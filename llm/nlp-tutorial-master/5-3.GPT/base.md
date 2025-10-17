# GPT 模型关键知识

## 1. 架构基础

* **Transformer 架构**：核心是 **多头自注意力（Multi-Head Self-Attention）+ 前馈网络（FFN）**。
* **Decoder-only 堆叠**：GPT 只用 Transformer **解码器部分**（有 Masked Self-Attention，保证自回归）。
* **因果遮罩（Causal Mask）**：attention 矩阵中禁止看到未来 token，只能利用过去上下文。

## 2. 预训练目标

* **自回归语言建模（Autoregressive LM）**：最大化条件概率

  $$
  \prod_t P(x_t | x_{<t}; \theta)
  $$
* 不使用 BERT 的 Masked LM / NSP，而是完全基于**下一个词预测**。

## 3. 表示与输入

* **词向量嵌入（Token Embedding）**：最初用 BPE（Byte Pair Encoding），后续有 GPT-NeoX 等用 SentencePiece。
* **位置编码（Positional Encoding）**：GPT-1/2 使用固定正余弦，GPT-3 及之后用 **可学习位置编码**，GPT-NeoX/T5/PaLM 等引入 **RoPE (旋转位置编码)**。

## 4. 训练技术

* **大规模预训练数据**：从 BookCorpus/维基百科扩展到 WebText、Common Crawl、RedPajama 等。
* **优化器**：Adam/AdamW（权重衰减修正），学习率调度（warmup+余弦/线性衰减）。
* **正则化与稳定性**：残差连接、LayerNorm、Dropout、梯度裁剪。
* **混合精度**：FP16/bf16，提升训练速度与显存利用。

## 5. 模型扩展与改进

* **规模扩展**：GPT-1（117M）→ GPT-2（1.5B）→ GPT-3（175B），展示出**Scaling Law**（损失随模型/数据/算力对数线性下降）。
* **稀疏注意力**：为长上下文做优化（如 GPT-3 的 2k → GPT-4 的 32k/128k）。
* **分布式训练**：数据并行、模型并行、张量并行、流水线并行（Megatron-LM/DeepSpeed 技术）。

## 6. 对齐与增强（InstructGPT/ChatGPT/后续）

* **SFT（Supervised Fine-Tuning）**：在人工标注数据上做有监督微调。
* **RLHF（Reinforcement Learning with Human Feedback）**：奖励模型 + PPO 强化学习，让模型生成更符合人类偏好。
* **DPO/ORPO 等替代方法**：直接偏好优化，减少 RLHF 的复杂性。
* **工具与检索增强**：ChatGPT/Plugins、RAG（Retrieval-Augmented Generation）。

## 7. 应用与能力

* **Few-shot/Zero-shot 学习**：通过上下文提示（Prompt）解决任务。
* **Chain-of-Thought (CoT)**：逐步推理提示增强模型逻辑推理。
* **自一致性 (Self-Consistency)**、**树搜索 (Tree-of-Thoughts)**、**循环思维链 (Reflexion)** 等增强推理。

---

✅ 总结一句话：
GPT 模型的关键知识包括 **Transformer decoder-only 架构、因果遮罩的自回归目标、位置编码、子词分词、优化器与大规模训练技术、Scaling Law、RLHF 与对齐方法**，以及后续衍生的 **提示工程、长上下文建模与检索增强** 等。
