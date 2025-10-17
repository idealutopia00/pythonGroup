# 🌐 LLM 微调与推理增强方法综述

## 1. 🔹 SFT（Supervised Fine-Tuning）监督微调

* **目的**：用人工标注/合成的「指令-响应」数据，把 base LLM 调整为符合人类指令的模型。
* **数据构造**：

  * **指令数据**（instruction）：开放问答、对话、多任务。
  * **比对数据**：问答对、摘要、翻译、代码任务。
  * **数据比例**：一般 **通用数据 : 专业数据 = 7:3 或 8:2**，保证通用能力和专业任务兼顾。
* **全参微调**：更新所有参数，效果最好但代价大，需要大显存和长训练时间。
* **冻结微调**：冻结主干，仅更新一小部分（embedding/层归一化/Adapter等），节省算力。

---

## 2. 🔹 PEFT（Parameter-Efficient Fine-Tuning）高效微调

在保持大部分参数冻结的情况下，只训练很小一部分附加参数。

### 常见方法：

1. **Prompt Tuning**

   * 学习一小串连续可训练的「虚拟 token」，作为提示拼接到输入前。
   * 缺点：需要较多样本，泛化差。

2. **P-Tuning v2**

   * 在 Transformer 每一层插入连续可训练 embedding。
   * 优点：比单纯 prompt tuning 更稳定，效果接近 LoRA。

3. **Prefix-Tuning**

   * 为每一层注意力引入可训练 prefix key/value。
   * 优点：高效，训练参数极少；缺点：可能对小数据集敏感。

4. **Adapter-Tuning**

   * 在每一层插入瓶颈 MLP（小模块），只训练 adapter 参数。
   * 优点：灵活，能与多任务共存。

5. **LoRA（Low-Rank Adaptation）及变体**

   * 将权重矩阵分解为低秩形式 $W + AB^T$，只训练小矩阵 $A,B$。
   * 优点：目前工业界最常用，参数效率高，效果好。
   * **变体**：

     * **QLoRA**：结合量化（如 4bit），在单卡消费级 GPU 上也能微调大模型。
     * **DoRA/LoRA+**：对正交/分布做改进，进一步提高效果。

---

## 3. 🔹 推理增强策略（Reasoning）

### 1) **CoT（Chain of Thought）思维链**

* 通过提示让模型「分步推理」，而不是直接输出答案。
* 常见模板：**“Let's think step by step.”**
* 优点：显著提升数学、逻辑推理能力。

### 2) **Self-Consistency**

* 运行多条 CoT 推理路径 → 投票选结果。
* 优点：减少随机性，提高正确率。

### 3) **ReAct（Reason + Act）**

* 结合 **推理轨迹** 和 **外部工具调用**，提升复杂任务表现。

### 4) **o1 系列（OpenAI 新路线）**

* **o1-preview / o1-mini** 强调通过 **推理专用训练 + 长上下文 + CoT 强化**，提升数学、逻辑、规划任务能力。
* 背后技术：

  * 大规模 **推理数据集**（带步骤解释）
  * **RLHF/DPO** 不仅优化回答，还优化推理链条的质量。
  * **自我验证 / 反思（Reflexion, Verification）**：让模型检查并修正自己的推理。

---

## 4. ✅ 总结与推荐学习路径

1. **SFT** → 了解全参微调 vs 冻结微调，理解数据比例设计。
2. **PEFT** → 熟悉 LoRA/QLoRA（最实用），再理解 Prompt/Prefix/Adapter/P-Tuning。
3. **Reasoning** → 掌握 CoT 基础，再看 Self-Consistency、ReAct、o1 系列的「推理对齐」方法。

---

要不要我帮你画一张 **思维导图**，把「SFT → PEFT → Reasoning」这些方法的关系和代表性技术串起来？
