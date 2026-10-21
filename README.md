# 社会学研究方法 · Social Science Research Methods

一个用于**社会学研究方法**的 AI 技能包：六条证据路线、一套全流程设计器、一份百分制评审量表。

适用于七类场景：

1. 研究方法知识科普与概念解释
2. 用方法视角解读社会现象
3. 解答方法专业问题（含"什么时候不成立"）
4. 系统学习研究方法知识点
5. 探讨方法论方向的研究选题
6. 撰写实证论文时做正确的研究设计
7. 评估论文或课题的研究设计质量

---

## 核心设计

**六条证据路线**——先问"你要哪一类证据"，再谈方法：

| 路线 | 回答什么 |
|---|---|
| ① 描述与总体 | 总体长什么样、有多大把握 |
| ② 因果识别 | 是不是 X 造成了 Y |
| ③ 关联与建模 | 控制条件下 X 与 Y 是什么关系 |
| ④ 机制与过程 | 事情怎样一步步发生 |
| ⑤ 概念与测量 | 概念到底指什么、测到了没有 |
| ⑥ 新型数据与预测 | 用痕迹数据与模型能说什么 |

**为什么按路线而不是按方法组织**：社会科学里绝大多数设计错误，不是技术用错，而是**问题与证据类型错配**——用横断面数据回答过程问题，用回归系数回答总体分布问题，用访谈回答"有多少比例"的问题。

**一条核心行为**：遇到解读现象、探讨选题、撰写方法节、评审设计时，先问路线，只问一次，并把六条路线的差别讲清楚。

---

## 内容结构

```
social-science-research-methods/
├── SKILL.md                                  # 入口：路线速查、路由协议、七类场景工作流、Gotchas
├── README.md
├── LICENSE
├── CHANGELOG.md
├── references/
│   ├── 01-knowledge-map.md                   # 方法全景、四层结构、九步流程、24 道自测
│   ├── 02-question-to-design.md              # 核心路由：问句→路线→设计矩阵、错配诊断
│   ├── 03-concepts-and-measurement.md        # 概念化、测量层次、信度效度、题项六缺陷
│   ├── 04-sampling-generalization.md         # 抽样框、总误差框架、无应答、加权、概化
│   ├── 05-causal-inference.md                # 反事实、七种识别、控制变量决策清单
│   ├── 06-modeling-and-diagnostics.md        # 回归三解读、函数形式、共线性、模型评估
│   ├── 07-inference-and-uncertainty.md       # p 值、区间、功效、多重比较、基率
│   ├── 08-mechanism-case-comparison.md       # 案例、比较、集合论、过程追踪
│   ├── 09-mixed-methods.md                   # 混合方法设计与整合三层次
│   ├── 10-methodology-and-philosophy.md      # 本体论、推理逻辑、说法与做法
│   ├── 11-new-data-and-online.md             # 大数据、复杂性、在线研究、伦理
│   ├── 12-writing-the-design.md              # 方法节七件套 + 句式模板
│   ├── 13-review-rubric.md                   # 六维百分制评审量表
│   ├── 14-cases-and-glossary.md              # 五个现象案例 + 术语表 + 20 条误读纠错
│   └── audit.md                              # 依据强度与核对说明
├── assets/
│   ├── design-canvas.md                      # 一页纸研究设计画布
│   └── checklist.md                          # 投稿前设计自查 40 项
└── scripts/
    └── audit.py                              # 包结构与内容自检
```

---

## 三条贯穿全流程的原则

1. **先说清"这句话能说到多硬"。** 结论只落在四级：描述 / 关联 / 因果 / 机制。**四级之间不能免费升级**，动词必须与级别匹配。
2. **识别假设永远逐条写出。** 说不出假设，就等于没有设计。
3. **把"控制"当设计问题，不当变量堆叠问题。** 加控制变量不能修复未测混杂。

---

## 安装

把整个目录放进你的技能目录即可：

```bash
# 项目级
cp -r social-science-research-methods <project>/.workbuddy/skills/

# 用户级
cp -r social-science-research-methods ~/.workbuddy/skills/
```

自检：

```bash
python scripts/audit.py .
```

---

## 版本

v1.0.0 — 首次发布。六路线、15 个 references、2 个模板、1 个自检脚本。

---

## 许可

保留所有权利（All rights reserved）。可原样自由复制与分发（须保留许可与署名）；用于个人学习、教学与研究。商业使用或改编分发请先联系作者。
