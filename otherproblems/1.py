import pygame
import numpy as np
import math

# ================= 配置区域 =================
SAMPLE_RATE = 44100
DURATION = 1.0       # 每个音符的持续时间（秒）
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
ACTIVE_COLOR = (100, 200, 255) # 按下时的颜色（天蓝色）
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 300

# ================= DSP 音频生成核心 =================
def generate_tone(frequency, duration=1.0, volume=0.5):
    """
    使用 NumPy 生成带有简单包络的正弦波，模拟钢琴的衰减感
    """
    n_samples = int(SAMPLE_RATE * duration)
    t = np.linspace(0, duration, n_samples, False)
    
    # 1. 生成纯正弦波
    wave = np.sin(2 * np.pi * frequency * t)
    
    # 2. 添加“泛音”让声音更丰富 (叠加一个低音量的二次谐波)
    overtone = 0.5 * np.sin(2 * np.pi * (frequency * 2) * t)
    wave += overtone
    
    # 3. 添加包络 (Envelope): 声音应该是一开始大，然后指数衰减
    # 这是一个简单的指数衰减函数
    envelope = np.exp(-3 * t) 
    wave = wave * envelope
    
    # 4. 归一化并转换为 16-bit 格式
    wave = wave * volume * 32767 / np.max(np.abs(wave))
    return wave.astype(np.int16)

# ================= 键盘映射逻辑 =================
# 定义按键与音名、频率的映射关系
# 键位布局：A S D F G H J K L
KEY_MAP = {
    pygame.K_a: {'note': 'Do', 'freq': 261.63, 'label': 'A'},
    pygame.K_s: {'note': 'Re', 'freq': 293.66, 'label': 'S'},
    pygame.K_d: {'note': 'Mi', 'freq': 329.63, 'label': 'D'},
    pygame.K_f: {'note': 'Fa', 'freq': 349.23, 'label': 'F'},
    pygame.K_g: {'note': 'Sol', 'freq': 392.00, 'label': 'G'},
    pygame.K_h: {'note': 'La', 'freq': 440.00, 'label': 'H'},
    pygame.K_j: {'note': 'Ti', 'freq': 493.88, 'label': 'J'},
    pygame.K_k: {'note': 'Do+', 'freq': 523.25, 'label': 'K'},
    pygame.K_l: {'note': 'Re+', 'freq': 587.33, 'label': 'L'},
}

class PianoKey:
    def __init__(self, rect, config):
        self.rect = rect
        self.note_name = config['note']
        self.freq = config['freq']
        self.label = config['label']
        self.is_pressed = False
        
        # 预生成音频数据对象
        # 立体声需要在数组上做一些变换，这里我们简单处理为单声道转立体声
        tone_data = generate_tone(self.freq, DURATION)
        # 将单声道数据复制一份给双声道
        stereo_tone = np.column_stack((tone_data, tone_data))
        # 转换为 Pygame 声音对象
        self.sound = pygame.sndarray.make_sound(stereo_tone)

    def draw(self, surface):
        # 决定颜色
        color = ACTIVE_COLOR if self.is_pressed else WHITE
        
        # 绘制琴键背景
        pygame.draw.rect(surface, color, self.rect)
        # 绘制边框
        pygame.draw.rect(surface, BLACK, self.rect, 2)
        
        # 绘制文字 (音名 + 键盘按键)
        font_note = pygame.font.SysFont("Arial", 24, bold=True)
        font_key = pygame.font.SysFont("Arial", 18)
        
        text_note = font_note.render(self.note_name, True, BLACK)
        text_key = font_key.render(f"[{self.label}]", True, (100, 100, 100))
        
        # 居中显示
        surface.blit(text_note, (self.rect.centerx - text_note.get_width() // 2, self.rect.bottom - 60))
        surface.blit(text_key, (self.rect.centerx - text_key.get_width() // 2, self.rect.bottom - 30))

    def press(self):
        if not self.is_pressed:
            self.is_pressed = True
            self.sound.stop() # 防止重复叠加太乱，先停再放
            self.sound.play(fade_ms=50)

    def release(self):
        self.is_pressed = False
        self.sound.fadeout(300) # 松手时声音平滑淡出

def main():
    pygame.init()
    pygame.mixer.init(frequency=SAMPLE_RATE, size=-16, channels=2, buffer=512)
    
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Python 极简钢琴 (Mac版)")
    
    # --- 初始化琴键对象 ---
    keys = []
    num_keys = len(KEY_MAP)
    key_width = WINDOW_WIDTH // num_keys
    
    # 按照 KEY_MAP 的顺序（A, S, D...）创建琴键
    # 注意：字典是无序的，我们需要按列表顺序来排版
    ordered_key_codes = [pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_f, 
                         pygame.K_g, pygame.K_h, pygame.K_j, pygame.K_k, pygame.K_l]
    
    for i, key_code in enumerate(ordered_key_codes):
        config = KEY_MAP[key_code]
        rect = pygame.Rect(i * key_width, 0, key_width, WINDOW_HEIGHT)
        piano_key = PianoKey(rect, config)
        # 将对象存入字典，方便通过 key_code 快速查找
        KEY_MAP[key_code]['obj'] = piano_key
        keys.append(piano_key)

    running = True
    clock = pygame.time.Clock()

    while running:
        # 1. 事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # 按下键盘
            elif event.type == pygame.KEYDOWN:
                if event.key in KEY_MAP:
                    KEY_MAP[event.key]['obj'].press()
                # 按 ESC 退出
                if event.key == pygame.K_ESCAPE:
                    running = False
            
            # 松开键盘
            elif event.type == pygame.KEYUP:
                if event.key in KEY_MAP:
                    KEY_MAP[event.key]['obj'].release()

        # 2. 绘制界面
        screen.fill(BLACK)
        for key_obj in keys:
            key_obj.draw(screen)
        
        # 3. 刷新显示
        pygame.display.flip()
        clock.tick(60) # 保持 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()