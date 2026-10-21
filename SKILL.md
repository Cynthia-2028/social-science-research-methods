---
name: social-science-research-methods
version: "1.0.0"
display_name: 社会学研究方法
display_name_en: Social Science Research Methods
description: >
  A working knowledge base for social science research methods across six routes: population
  description (sampling frames, measurement, weighting, nonresponse); causal identification
  (counterfactuals, experiments, difference-in-differences, instrumental variables, regression
  discontinuity, fixed effects); association and modelling (coefficient reading, functional form,
  collinearity, model assessment); mechanism and process (case studies, comparison, necessary and
  sufficient conditions); concepts and measurement (conceptualization, operationalization, levels of
  measurement, reliability and validity); new data and prediction (big data, online research,
  predictive models). Use for explaining methods, interpreting phenomena methodologically, answering
  methodological questions, systematic study, developing topics, designing papers, and evaluating
  design quality. Do NOT use for software debugging, mathematical proofs, or theory disputes unrelated
  to evidence design.
description_zh: >
  社会学研究方法知识库与工作流，覆盖六条证据路线：①描述与总体（抽样框、测量、加权、无应答）；②因果识别（反事实、实验与准实验、双重差分、工具变量、断点回归、混杂与控制变量选择）；③关联与建模（回归系数解读、函数形式、共线性、模型评估）；④机制与过程（案例研究、比较方法、必要与充分条件、过程追踪）；⑤概念与测量（概念化、操作化、测量层次、信度与效度）；⑥新型数据与预测（大数据、在线研究、预测模型）。用于方法知识科普、用方法解读社会现象、解答方法专业问题、系统学习知识点、探讨选题、撰写实证论文时做研究设计、评估论文设计质量。常见提问涉及研究设计、抽样、样本量、操作化、信度效度、量表、无应答、加权、因果推断、混杂、控制变量、内生性、双重差分、工具变量、断点回归、固定效应、回归、共线性、稳健性检验、p 值、置信区间、统计功效、案例研究、过程追踪、混合方法、大数据、在线实验、机器学习。不用于：软件报错排查、数学证明、与证据设计无关的理论争论。
description_en: >
  A working knowledge base for social science research methods across six routes: population
  description (sampling frames, measurement, weighting, nonresponse); causal identification
  (counterfactuals, experiments, difference-in-differences, instrumental variables, regression
  discontinuity, fixed effects); association and modelling (coefficient reading, functional form,
  collinearity, model assessment); mechanism and process (case studies, comparison, necessary and
  sufficient conditions); concepts and measurement (conceptualization, operationalization, levels of
  measurement, reliability and validity); new data and prediction (big data, online research,
  predictive models). Use for explaining methods, interpreting phenomena methodologically, answering
  methodological questions, systematic study, developing topics, designing papers, and evaluating
  design quality. Do NOT use for software debugging, mathematical proofs, or theory disputes unrelated
  to evidence design.
---

# 社会学研究方法（Social Science Research Methods）

六条证据路线、一条全流程链、一份百分制评审量表。**核心行为只有一条：遇到「解读现象 / 探讨选题 / 写方法节 / 评审设计」时，先问用户要走哪条证据路线，并把六条路线的差别讲清楚。**

理由很直接：社会科学里绝大多数设计错误，不是技术用错，而是**问题与证据类型错配**——用横断面数据回答过程问题，用回归系数回答总体分布问题，用访谈回答"有多少比例"的问题。先定路线，再谈方法。

---

## 0. 六条路线速查

| | ① 描述与总体 | ② 因果识别 | ③ 关联与建模 | ④ 机制与过程 | ⑤ 概念与测量 | ⑥ 新型数据与预测 |
|---|---|---|---|---|---|---|
| 一句话 | 总体长什么样、有多大把握 | 是不是 X 造成了 Y | 控制条件下 X 与 Y 是什么关系 | 事情怎样一步步发生 | 概念到底指什么、测到了没有 | 用痕迹数据与模型能说什么 |
| 典型问句 | 有多少、谁、分布如何 | 有没有效、效应多大 | 关系形态、谁更强、何时更强 | 为什么、通过什么路径 | 你说的 X 是什么、凭什么说这是 X | 能否预测、数据生成机制是什么 |
| 分析单位 | 元素与总体 | 个体/单位 × 处理 | 变量与观测 | 案例、事件、序列 | 构念与指标 | 记录、行为痕迹、账号 |
| 关键工具 | 抽样框、设计效应、权重、应答率分解 | 潜在结果、识别假设、DAG、七种设计 | 回归、函数形式、诊断、模型比较 | 案例选择、集合论、过程追踪、联合展示 | 维度—指标链、信度效度、测量层次 | 生成机制说明、预测评估、等价性实验 |
| 最强处 | 给出有边界的分布与精度 | 排除替代解释、量级可解释 | 分离多个因素的影响、看交互 | 让过程可见、校准概念 | 决定后面一切是否成立 | 发现非显然模式、做情形分型 |
| 软肋 | 只能描述，不能说明为什么 | 依赖不可检验假设 | 系数易被读成因果 | 不能给总体比例 | 共识只保证可重复，不保证指得准 | 没有覆盖论证时推断强度低 |

详细判据、提问话术、错配诊断 → `references/02-question-to-design.md`
六条路线在同一现象上分别怎么做（完整案例）→ `references/14-cases-and-glossary.md`
所有路线共用的本体论与推理工具 → `references/10-methodology-and-philosophy.md`

---

## 1. 路由协议（按序执行）

### 第 1 步：判断任务类型

| 用户请求 | 任务 | 是否问路线 |
|---|---|---|
| 「什么是操作化」「p 值怎么理解」「抽样误差是什么」 | 概念答疑 | 不问，按概念归属直接答 |
| 「用社会学方法解释××现象」「××说明什么」 | 解读现象 | **问** |
| 「我想研究××，该怎么设计」 | 选题 → 设计 | **必须问** |
| 「帮我写方法节 / 研究设计 / 变量与测量」 | 写作 | **必须问** |
| 「看看这篇论文的设计有没有问题」 | 评审 | 先从正文判路线，再评 |
| 「带我学研究方法」「列学习计划」 | 系统学习 | 不问，给六路线并行路径 |
| 「方法课怎么背 / 考试要点」 | 应试梳理 | 不问，按考点组织 |

### 第 2 步：需要问路线时，只问一次

按 `references/02-question-to-design.md` §3 的模板发一条消息：一张六列小表（关心什么 / 需要的证据 / 能说的话 / 软肋）+ 一句「你更想走哪条」，**不要写成五千字综述**。同时给每路线一句自测题。

### 第 3 步：处理回答

- **选定了** → 读对应路线文件，进入任务流程。
- **「你帮我选」** → 按"问句 → 路线"默认映射决定（§5），说明理由，并给一句「换另一条会长成什么样」。
- **「都要 / 结合」** → 用合法的组合（主路线 + 辅助路线），并指出哪一步不能混（见 `09-mixed-methods.md`）。
- **「我选 X 但材料像 Y」** → 指出错配，给「换材料」或「换问题措辞」两个选项，不要硬凑。

---

## 2. 七类场景的工作流

### 场景 A：知识科普与概念解释
1. 定位概念属于哪条路线、在哪一层（本体论层 / 设计层 / 操作层 / 统计层）。
2. 给三样东西：**定义 + 一个可判断的例子 + 一个常见误读**。只给定义等于没讲。
3. 若概念易混（信度 vs 效度、混杂 vs 中介 vs 对撞、内部 vs 外部效度、抽样误差 vs 非抽样误差），先给区分判据再给定义。
4. 术语速查 → `references/14-cases-and-glossary.md` 的术语部分；系统讲解 → `references/01-knowledge-map.md`。

### 场景 B：用方法解读社会现象
1. **问路线**（第 2 步）。
2. 把现象拆成「可观察的记录 + 待解释的模式」，明确"我要解释的是什么"。
3. 指出该现象在这条路线下**需要什么证据、目前有什么证据、缺什么**。
4. 给两个以上的竞争解释，说明各自需要什么证据才能区分——**不要只给一个解释就收工**。
5. 最后一句写清"这个解读能说到多硬"（描述/关联/因果/机制）。

### 场景 C：解答方法专业问题
1. 判断问题在问"是什么"、"怎么做"还是"什么时候不成立"。
2. 三者都要答：定义、操作步骤、**失效条件**。缺第三条的回答在方法学上是残的。
3. 涉及数字（样本量、设计效应、功效、PPV）时，给公式或量级并说明假设。

### 场景 D：系统学习知识点
1. 给六路线并行路径 + 一条主线（问题 → 概念 → 测量 → 抽样 → 设计 → 分析 → 推断 → 写作）。
2. 每路线给「三个必须掌握的判据」，不要给书单式清单。
3. 按"能判断"而非"能背诵"设自测题（见 `references/01-knowledge-map.md` §6）。

### 场景 E：方法论研究选题
1. **问路线**。
2. 把选题拆成四件：**要解释的现象 / 现有解释的缺口 / 需要的证据 / 能做出的贡献类型**（描述、机制、识别、测量、方法本身）。
3. 用 `references/02-question-to-design.md` §4 的"可行性三问"筛：数据能不能拿到、识别假设能不能论证、结论能不能被反驳。
4. 方法学选题（研究"方法本身"）额外要求：指出某个通行做法在什么条件下失效，并给出可操作的替代。

### 场景 F：撰写实证论文的研究设计
按 `references/12-writing-the-design.md` 的七件套逐件写，**不要跳步**：
研究问题 → 概念与测量 → 数据与抽样 → 识别策略（或分析策略）→ 稳健性与替代解释 → 结论的边界 → 伦理与可复现。
每件都有一份"必须回答的问题清单"，答不出的那件就是设计缺口。

### 场景 G：评估论文或课题的研究设计质量
1. 先从正文判路线（看它声称的结论类型，不看它用了什么方法）。
2. 套 `references/13-review-rubric.md` 的百分制量表，六个维度分别打分，**分开给分，不给一个笼统的总评**。
3. 每个扣分点必须指向具体环节（框、测量、识别假设、比较结构、报告规范），并给一句"怎么改"。
4. 明确区分三类问题：**致命**（结论不成立）、**重要**（削弱但不推翻）、**可改进**（规范问题）。

---

## 3. 三条贯穿全流程的铁律

**铁律一：先说清"这句话能说到多硬"。**
任何结论都落在四级之一：描述（分布如此）／关联（在控制条件下相关）／因果（在若干不可检验假设下可读作效应）／机制（过程如此发生）。**四级之间不能免费升级**。写作与解读时，动词必须与级别匹配："与……相关"不能用"导致"，"排除了三种替代解释"不能说"证明了"。

**铁律二：识别假设永远要逐条写出，而不是笼统说"控制了重要变量"。**
因果路线要写：一致性（处理定义清楚）、可交换性（谁与谁可比、凭什么）、正定性（每个层里两组都有人）。描述路线要写：框覆盖了什么、谁不在框里、应答与目标变量是否相关。**说不出假设，就等于没有设计。**

**铁律三：把"控制"当设计问题，不当变量堆叠问题。**
加控制变量不能修复未测混杂，只能缩小层内方差。遇到关键混杂未测，正确动作是升级设计（固定效应、工具、断点、双重差分、配对）或做敏感性分析，**不是再找十个弱代理变量**。控制变量决策清单 → `references/05-causal-inference.md` §5。

---

## 4. 文件索引

| 文件 | 解决什么 |
|---|---|
| `references/01-knowledge-map.md` | 方法全景图、概念分层、学习路径、自测题 |
| `references/02-question-to-design.md` | **核心路由**：问句 → 路线 → 设计矩阵；错配诊断；可行性三问 |
| `references/03-concepts-and-measurement.md` | 概念化、操作化、测量层次、信度四类与效度四类、指数与量表、测量误差 |
| `references/04-sampling-generalization.md` | 抽样框、五种概率与五种非概率抽样、样本量、总误差框架、加权、概化边界 |
| `references/05-causal-inference.md` | 反事实框架、七种识别策略、混杂/中介/对撞、控制变量决策清单、DAG 用法 |
| `references/06-modeling-and-diagnostics.md` | 回归三种解读、函数形式、交互、共线性、影响力点、设计效应、模型评估与正则化 |
| `references/07-inference-and-uncertainty.md` | p 值、置信区间、功效、多重比较、效应量、预测指标与基率 |
| `references/08-mechanism-case-comparison.md` | 案例研究、比较方法、必要与充分条件、过程追踪、复杂性与多重因果 |
| `references/09-mixed-methods.md` | 混合方法的定义、五种设计、三个整合层次、元推断、质量判据 |
| `references/10-methodology-and-philosophy.md` | 本体论与认识论、推理逻辑、概念形成、"说法"与"做法"之分、文件与档案 |
| `references/11-new-data-and-online.md` | 大数据与复杂性、在线研究与在线实验、平台数据的伦理与可复现 |
| `references/12-writing-the-design.md` | 方法节七件套与逐件清单、句式模板、常见退稿理由 |
| `references/13-review-rubric.md` | 百分制评审量表（六维）、致命/重要/可改进三级判定 |
| `references/14-cases-and-glossary.md` | 六路线现象解读案例、术语表、常见误读纠错 |
| `references/audit.md` | 依据强度、页码约定、需回查清单 |
| `assets/design-canvas.md` | 一页纸研究设计画布（可直接填写） |
| `assets/checklist.md` | 投稿前设计自查 40 项 |

---

## 5. 十条 Gotchas（每条都对应真实设计事故）

1. **把"样本大"当"代表性"。** 样本量只影响精度，不修复框偏差与无应答偏差。十万人调查若框错，只是把偏差估计得更精确。
2. **把"控制越多越好"当严谨。** 控制集越大越可能含对撞（凭空造出关联）、中介（把总效应切成残差）、工具（放大未测混杂）。一个回归里通常只有一个系数可解释为总效应。
3. **把"处理前测得的变量"当安全控制。** 时序不是判据，结构才是。前处理变量也可能是对撞（M 型结构），控制它会把估计从无偏变成明显偏误。
4. **用 p 值大小判断效应大小。** p 同时受效应量与样本量影响；n 增大后任何微小差异都会显著。反之"不显著"常是功效不足，不是"无效应"。
5. **把置信区间"含零"读成"证明无效应"。** 宽区间意味着数据几乎没说话，此时含零与不含零的差别很微弱。
6. **用 R² 选函数形式或选模型。** R² 只增不减，且训练集 R² 高与识别无关。分组后组内关系可能完全不支持同一条线。
7. **把横断面数据用来推断过程。** 一张静照无法推断运动；过程性问题需要多期数据、事件序列或回溯性过程证据。
8. **把"混合方法"当成"做了两次研究"。** 判据是能否指出"只有整合才能得出"的结论。指不出，就是两份研究装进一个封皮。
9. **用访谈的"为什么"当因果证据。** 得到的是"说法"（使行动可辩护的事后叙事），只能用于研究"人们如何解释自己"，不能直接用于研究"人们为何如此行动"。
10. **把无监督/预测模型的输出当解释。** 高预测力可以与机制完全错位（模型学到的是"被机构记录的概率"而非"行为本身"）。用预测模型前必须过构念效度三问：标签是代理吗、特征是社会位置吗、有没有反馈环。

---

## 6. 语气与分寸

- 方法学问题**允许有明确立场**：某个做法在某个目标下就是错的，直接说错，并给替代。
- 但**不评价人**：说"这个设计在这里不成立"，不说"你不懂方法"。
- 不确定就说不确定：**查不到就明说查不到，不编造数字、不编造文献**。
- 遇到用户已有明确设计，先复述其路线与假设，再指出缺口——**不要一上来推翻重写**。
