# Human-AI Collaborative Game Testing with Vision Language Models 

_An Experiment Report_ 

|Boran Zhang|Muhan Xu|Zhijun Pan<sup>_∗_</sup>|
|---|---|---|
|_Zhengzhou University_|_University of the Arts London_|_Royal College of Art_|
|Zhengzhou, China|London, United Kingdom|London, United Kingdom|
|zhangboran12138@gs.zzu.edu.cn|m.xu0920221@arts.ac.uk|zhijun.pan@network.rca.ac.uk|



**_Abstract_ —As modern video games become increasingly complex, traditional manual testing methods are proving costly and inefficient, limiting the ability to ensure high-quality game experiences. While advancements in Artificial Intelligence (AI) offer the potential to assist human testers, the effectiveness of AI in truly enhancing real-world human performance remains underexplored. This study investigates how AI can improve game testing by developing and experimenting with an AI-assisted workflow that leverages state-of-the-art machine learning models for defect detection. Through an experiment involving 800 test cases and 276 participants of varying backgrounds, we evaluate the effectiveness of AI assistance under four conditions: with or without AI support, and with or without detailed knowledge of defects and design documentation. The results indicate that AI assistance significantly improves defect identification performance, particularly when paired with detailed knowledge. However, challenges arise when AI errors occur, negatively impacting human decision-making. Our findings show the importance of optimizing human-AI collaboration and implementing strategies to mitigate the effects of AI inaccuracies. By this research, we demonstrate AI’s potential and problems in enhancing efficiency and accuracy in game testing workflows and offers practical insights for integrating AI into the testing process.** 

**_Index Terms_ —Artificial Intelligence, Game Testing, HumanAI Collaboration, Test Automation, Error Detection, Process Optimization.** 

## I. INTRODUCTION 

The rapid growth of the gaming industry has led to the development of increasingly complex and immersive video games, characterized by dynamic mechanics, interactive narratives, and expansive open worlds [1]–[4]. Ensuring the functionality and quality of such intricate games requires comprehensive testing. However, traditional manual game testing approaches are becoming insufficient due to the scale and complexity of modern games. These methods are timeconsuming, resource-intensive, and prone to human error, reducing their effectiveness in identifying a broad range of defects [5]–[7]. 

While average gamers can serve as video game playtesters, Artificial Intelligence (AI) has emerged as a promising solution to enhance game testing workflows by automating defect 

_∗_ Corresponding author. 

detection processes and reducing reliance on manual efforts. Early AI approaches in game testing focused on rule-based automation to manage repetitive tasks like regression testing. However, these systems struggled to adapt to the emergent gameplay dynamics and player behaviors found in complex gaming environments [1], [8], [9]. Recent advancements in machine learning, particularly reinforcement learning, have enabled AI systems to autonomously simulate player interactions and learn from game environments, improving both the realism and robustness of test cases [6], [10]–[13]. These AI systems are capable of detecting a wide spectrum of defects, ranging from visual glitches to gameplay inconsistencies, enhancing the depth and efficiency of game testing. 

A key advancement in AI-driven testing is the integration of multimodal inputs—visual, audio, and textual data—which allows AI systems to comprehensively analyze gameplay environments. By leveraging these diverse data types, AI systems can detect graphical anomalies, such as texture misalignments and rendering errors, while simulating player behaviors to uncover gameplay issues [3], [7], [14]–[18]. However, while AI systems offer enhanced capabilities, they also present challenges, particularly in misinterpreting complex game elements, which can lead to inaccurate defect identification or even hallucinations—where the AI erroneously flags non-defective elements as bugs. These hallucinations, compounded by human testers’ reliance on AI, can further complicate the testing process [19]–[23]. Solutions to mitigate AI hallucinations are actively being explored to enhance the reliability of AI systems [24], [25]. 

Current AI-driven game testing approaches can be classified into two main categories: rule-based automation and AI-driven perception systems [26]. Rule-based systems, which simulate player actions by interacting directly with the game’s source code, require substantial technical expertise and may interfere with game performance during testing [3], [27]. In contrast, AI-driven perception systems utilize machine vision and multimodal models to detect visual defects, such as rendering errors, and analyze gameplay mechanics [12], [15]. While effective, these systems may still struggle with unpredictable player behavior and nuanced gameplay scenarios, areas where 

human testers excel [13], [16], [28]. 

Despite the advances in AI, the extent to which AI enhances human performance in real-world game testing, particularly under various conditions, remains underexplored. This study aims to address this gap by investigating the impact of AI on human testers’ performance across different levels of knowledge and experience, and by exploring how AI-generated insights can improve defect detection while managing risks like hallucinations. 

The contributions of our research are as follows: 

- **AI-Assisted Game Testing Workflow** : We present an AI-assisted workflow that integrates machine learning to detect defects in game visuals, user interfaces, and gameplay mechanics. 

- **Empirical Insights into Human-AI Collaboration** : Through a comprehensive user study, we provide empirical evidence demonstrating how AI enhances game testers under various conditions, especially when paired with detailed knowledge and human oversight. 

- **Analysis of AI Hallucinations and Error Impact** : We analyze how AI hallucinations and other errors impact human testers’ performance, offering strategies to mitigate over-reliance and reduce the effects of AI inaccuracies. 

- **Practical Guidelines for AI Integration** : Based on the findings, we propose practical recommendations for incorporating AI into game testing workflows, emphasizing the balance between AI assistance and human judgment. 

II. RELATED WORK 

## _A. Multimodal AI_ 

Multimodal AI involves integrating diverse data types—such as visual, audio, and textual inputs—into AI systems, enabling more robust and comprehensive analysis [15], [16]. In the context of game testing, multimodal AI facilitates the detection of a wide array of defects, from visual glitches to inconsistencies in gameplay and narrative [3], [14], [29]. This approach allows AI systems to assess multiple dimensions of a game simultaneously, improving the breadth and depth of testing. 

Recent advancements in deep learning models designed for multimodal inputs have significantly enhanced AI’s realtime, multidimensional capabilities in game testing [30]. These models can process complex game environments, evaluating everything from graphical fidelity to narrative coherence [6], [12], [31], [32]. However, integrating multiple data types introduces challenges, including the need for large and diverse datasets and the computational complexity required for realtime analysis [7], [17]. Moreover, the ”black-box” nature of many deep learning models raises concerns about explainability, which can hinder human testers’ trust in AI systems [20], [33]. 

Another notable challenge with multimodal AI systems is hallucinations—where the AI misinterprets game elements and flags non-existent bugs [22]. Addressing this issue is crucial for improving AI reliability. Recent research has explored 

techniques like contrastive learning and model fine-tuning to reduce hallucinations and improve AI accuracy in defect detection [23]–[25]. These efforts are essential to ensuring that AI-assisted systems remain trustworthy and efficient in complex game testing environments. 

## _B. Human-AI Collaboration_ 

Human-AI collaboration in software testing combines the strengths of automated AI systems and human testers’ intuitive judgment. AI excels at automating repetitive tasks, such as generating test cases and identifying specific types of defects, thereby enhancing the efficiency and scalability of testing processes [11], [34]. Human testers, on the other hand, contribute critical thinking, intuition, and the ability to manage complex or edge-case scenarios that are often difficult to automate [35]– [37]. 

In game testing, which often involves dynamic environments and unpredictable player behaviors, balancing human-AI collaboration is essential for thorough defect detection [1], [38]. Studies have shown that over-reliance on AI systems can lead testers to overlook subtle defects or unquestioningly accept incorrect AI outputs, underscoring the importance of workflows that allow for human oversight and critical assessment [20], [21]. To mitigate these issues, explainable AI (XAI) techniques have been explored to improve the transparency of AI systems, especially when errors, such as hallucinations, occur [19], [39], [40]. 

Recent studies indicate that machine input can heavily influence human decision-making, especially under cognitive limitations [41]. Trust between human testers and AI systems is vital for effective collaboration [42], and dissonance between human and machine understanding can cause inefficiencies [43]. Well-designed interfaces should enable testers to adjust or override AI decisions, minimizing the impact of AI errors [44], [45]. Improved AI training methods and handling uncertainty are essential to mitigate these issues [25]. 

## _C. AI-Assisted Game Testing_ 

AI-assisted game testing has evolved from rule-based automation to more advanced machine learning and reinforcement learning techniques [1], [8], [18], [46], [47]. Deep learning architectures, particularly convolutional neural networks (CNNs), have proven effective in detecting visual defects, such as texture misalignments and rendering errors [15]. Systems like AstroBug [13] and SUPERNOVA [16] utilize these models to analyze gameplay footage in real time, offering scalable solutions that outperform manual testing in several aspects. 

Reinforcement learning, which simulates diverse player behaviors, has also been successfully applied to uncover bugs related to game physics, balance, and interaction dynamics, often missed by traditional testing methods [12], [27], [33], [48]. This approach allows AI to explore edge cases and emergent gameplay behaviors, improving the thoroughness of game testing [6], [14]. 

Nevertheless, AI-assisted game testing faces limitations. AI systems may struggle with the unpredictability of complex 

game environments, potentially missing nuanced defects that require human interpretation [19], [45]. Human oversight is therefore critical for validating AI-generated reports and refining models to better handle complex scenarios [15], [49]. 

## III. METHODOLOGY 

## _A. Game Testing Workflow_ 

The primary objective of our research is to investigate how AI can effectively assist human testers in identifying defects in video games, focusing on integrating AI-driven automation with human oversight. We employed two principle workflows: a traditional manual testing process and an AI-assisted testing process. 

In the traditional game testing workflow (illustrated in Fig 1), the process starts with game development and the creation of a detailed test plan. This test plan outlines the objectives, requirements, and scope of testing, covering both game mechanics and graphical elements [50]. Human testers manually execute the test cases, aiming to identify defects such as graphical glitches, gameplay inconsistencies, and physics issues. Defects identified by testers are documented in a test report, which is then forwarded to developers for resolution. After the resolution, regression testing is conducted to ensure no new issues have been introduced. This workflow, although thorough, is resource-intensive, time-consuming, and prone to human error, particularly for large and complex games [5], [51]. 

In the AI-assisted testing workflow (illustrated in Fig 2), the process begins similarly with game development and test planning. However, during the test execution phase, an AI component captures in-game screenshots and analyzes them using state-of-the-art models. The AI system detects visual defects such as texture misalignments, clipping errors, and UI inconsistencies, and compiles these findings into an initial test report for human reviewers. Human testers then validate the AI-identified defects and focus on more complex issues like gameplay mechanics and physics behaviors, which may not be easily detectable by AI. This hybrid approach enables AI to handle repetitive, surface-level defect detection, allowing human testers to spend more time on in-depth analysis. The final test report combines both AI-generated and human-verified results, which are submitted to developers for resolution. 

This hybrid workflow represents our core research framework: an integration of automated detection with human validation in game testing. The setup allows us to explore the effectiveness of such a system in improving testing efficiency, accuracy, and overall human performance. 

## _B. Experiment Setup_ 

Our experiment was designed to validate the AI-assisted game testing system’s reliability and examine the effects of human-AI collaboration in identifying game defects. The experiment setup consists of the following components: the system, test cases, execution procedures, and scoring mechanisms. 


![](images/Zhang_2025_Human_AI_Collaborative_Game_Testing_with_Vision_Language_Models.pdf-0003-09.png)


<!-- Start of picture text -->
Regression<br>Develop<br>Developer Game<br>Compile<br>Execute and<br>Record Results<br>Test Plan Tester Test Report<br><!-- End of picture text -->

Fig. 1. Traditional Game Testing Workflow (Simplified) 


![](images/Zhang_2025_Human_AI_Collaborative_Game_Testing_with_Vision_Language_Models.pdf-0003-11.png)


<!-- Start of picture text -->
Regression<br>Develop Detect<br>Developer Game<br>AI Test Report<br>Compile<br>Execute and<br>Record Results<br>Test Plan Tester Test Report<br><!-- End of picture text -->

Fig. 2. AI-Assisted Game Testing Workflow (Simplified) 

_1) System:_ The AI-assisted system is based on the state-ofthe-art GPT-4o model [30], which was employed to process a diverse dataset of video game visuals, including different defect types and gameplay elements. The AI component functions by processing game screenshots, generating descriptions of the game environment, and detecting a set of predefined defect categories (see Table II). Human participants interact with this system during the testing phases, working the AI’s outputs to identify game defects. The system’s performance metrics include the accuracy of visual descriptions and defect identifications, with an 87.5% accuracy rate for scene descriptions and a 97.1% accuracy rate for defect detection under controlled conditions. 

_2) Test Cases and Execution:_ The experiment involved a total of 800 test cases, divided equally across four experimental conditions: No Knowledge, No AI Assistance (Manual); Knowledge, No AI Assistance (KA); No Knowledge, With AI Assistance (AIA); and Knowledge, With AI Assistance (KA+AIA). Each condition consisted of 200 test cases, and each participant took a total of 40 random cases—10 from each condition. This ensured that all participants experienced every possible combination of AI assistance and the availability of knowledge. 

In this experiment, “knowledge” refers to detailed information generated by the AI system, including explanations of potential defects identified by the AI (when AI involves), as well as the game design documentation related to the specific test cases. This knowledge helps participants understand the 

TABLE I 

DEMOGRAPHICS OF HUMAN PARTICIPANTS 

||M(SD) or n(%)|
|---|---|
|**Age**||
|Under 18|1(0.4%)|
|18–24 years|153 (55.4%)|
|25–30 years|104 (37.7%)|
|Over 30 years|18 (6.5%)|
|**Gaming Experience**||
|Yes|269 (97.5%)|
|No|7 (2.5%)|
|**Education Level**||
|High School or below|17 (6.2%)|
|Associate Degree|84(30.4%)|
|Bachelor’s Degree|160 (58%)|
|Master’s Degree or above|15 (5.4%)|



types of defects that may occur and provides context from the game’s design to assist in defect identification. 

Each test case involved the identification of defects from game images, with participants required to identify up to two defects per case. Defects were selected from four primary categories: graphical rendering errors, user interface (UI) errors, scene and object consistency errors, and object and physics behavior errors, which were further subdivided into specific types as described in Table II. While most test cases contains at least one defect to be identifies, around 10% of all cases are bug-free. 

Test execution followed a structured sequence, ensuring participants experienced both AI-assisted and non-AI-assisted conditions, as well as conditions with and without the detailed knowledge provided by the AI system. 

_3) Scoring Mechanism:_ Participants were scored based on their ability to correctly identify defects within each test case. The scoring system was designed to allocate a maximum of 10 points per test case, with 5 points awarded for each correctly identified defect. Incorrect or missed defect identifications resulted in no points for that particular defect. Bug-free cases come with 10 points initially. If the participant identified bugs for bug-free cases, there will be no point. Therefore, each participant could score a maximum of 400 points, with the average score recorded as 211 points and the highest as 395. This scoring mechanism enabled a comparative analysis of participants’ performance across different test conditions. 

## _C. Participants_ 

_a) Human Participants:_ : A total of 276 human participants were recruited via an online platform, with the average test duration being 6 minutes and 5 seconds. Among the participants, 55.4% were between 18 and 24 years old, and 97.5% reported prior gaming experience. For a detailed breakdown of participant demographics, see Table I. 

_b) AI Component:_ : The AI component functions as an additional participant in the testing process, utilizing advanced machine vision techniques to analyze and detect defects. 

Its performance, as mentioned, was rigorously evaluated for accuracy in both scene description and defect identification. 

## _D. Tasks_ 

The primary task for participants was to identify defects in the provided game visuals and classify them based on the defined categories. Defects were categorized into graphical rendering errors, UI errors, scene and object consistency errors, and object and physics behavior errors [52], as detailed in Table II. Participants were required to complete the task under four different experimental conditions. 

## _E. Conditions_ 

Our experiment was structured into four testing conditions that combined the AI system with the availability of detailed defect information and design documentation (knowledge): 

- **No Knowledge, No AI Assistance (Manual)** : Participants relied solely on observation without any detailed defect information or AI assistance. 

- **Knowledge, No AI Assistance (KA)** : Participants were provided with detailed explanations of potential defects identified by the AI, along with game design documentation related to the test cases. However, they performed the tests without direct AI assistance during execution. 

- **No Knowledge, With AI Assistance (AIA)** : Participants used the AI system for defect identification but did not have access to detailed defect information or game design documentation. 

- **Knowledge, With AI Assistance (KA+AIA)** : Participants had both the AI system’s assistance and access to detailed explanations of potential defects, as well as game design documentation for the test cases. 

## _F. Procedure_ 

The experimental procedure followed these steps: 

- **Pre-Test Briefing** : Participants were briefed on the experiment’s content and procedure. 

- **Test Execution** : Participants evaluated 10 randomly assigned game screenshots in each of the four conditions (Manual, KA, AIA, KA+AIA), following a predefined sequence. 

- **Data Collection** : Participants’ responses, including the difficulty of the game screenshots and the AI system’s evaluations, were recorded. 

- **Post-Test Feedback** : Participants provided feedback on their experience, including their understanding of the AI system and defect identification process. 

- **Incentive Mechanism** : Participants were incentivized with monetary rewards based on their performance, with bonuses for higher accuracy scores. 

## _G. Data Analysis Method_ 

- _1) Data Preprocessing:_ To ensure the validity and accuracy 

- of the data, the following preprocessing steps were conducted: 

- **Exclusion of Anomalous Times:** Each participant’s response duration was recorded, with an average analysis 

TABLE II 

CLASSIFICATION AND DEFINITIONS OF GAME BUGS 

|**Category**|**Bug Type**|**Definition**|**References**|
|---|---|---|---|
|Graphical Rendering<br>Errors|Missing Textures|Failure of texture assets to load properly, leading to objects<br>being rendered with placeholder colors or default textures.|[28], [45], [33],<br>[49], [34], [53]|
||Lighting/Shadow Artifacts|Anomalies in lighting or shadow calculations, such as in-<br>accurate shadow placement or improper light distribution,<br>affecting scene realism.||
||Clipping Issues|Objects that intersect or pass through other objects or envi-<br>ronmental boundaries, violating expected spatial constraints<br>(e.g., objects passing through walls).||
||Resolution or Scaling Anomalies|Visual distortion due to incorrect game resolution or object<br>scaling, leading to blurry textures or disproportionate object<br>sizes.||
||Texture Tiling Artifacts|Visual seams or repetition artifacts when the same texture is<br>tiled across large surfaces, disrupting visual continuity.||
|User<br>Interface<br>(UI)<br>Errors|UI Element Overlap|Overlapping or improperly aligned UI elements (e.g., buttons,<br>text), resulting in reduced clarity and hindered user interac-<br>tion.|[34], [49]|
||Display Artifacts|Rendering issues within the UI, such as misaligned elements<br>or text, negatively affecting interface usability and informa-<br>tion accessibility.||
|Scene<br>and<br>Object<br>Consistency Errors|Missing or Deformed Objects|Incomplete or improperly rendered in-game objects, leading<br>to visual deformities or missing elements within the game<br>environment.|[6], [46], [10]|
||Scene Loading Errors|Incomplete or misaligned loading of the game environment,<br>such as unrendered terrain or structures, resulting in visual<br>dissonance.||
|Object<br>and<br>Physics<br>Behavior Errors|Abnormal Object Movement|Unnatural object or character movement, such as erratic<br>position shifts or paths that contradict expected physical<br>behavior.|[49], [15]|
||Physics Engine Errors|Errors in the physics simulation, where objects behave con-<br>trary to physical laws, such as passing through solid objects<br>or bouncing incorrectly.||
|No Bug|N/A|The game environment functions as expected with no de-<br>tectable graphical, UI, consistency, or physics-related issues.|N/A|



time per case exceeding 8 seconds. Therefore, any response time under 300 seconds was considered indicative of insufficient engagement. A minimum threshold of 300 seconds was established, and all records falling below this threshold were excluded. 

- **Handling of Score Anomalies:** Total scores for each participant underwent Z-score normalization. Records with absolute Z-scores greater than 3 were classified as outliers and removed. 

_2) Calculation of Accuracy:_ To evaluate participants’ performance under the four testing conditions—Manual (M), Knowledge Assistance (KA), AI Assistance (AIA), and Knowledge plus AI Assistance (KA+AIA)—we calculated the accuracy of defect identification. 

Let _K_ = _{_ M _,_ KA _,_ AIA _,_ KA+AIA _}_ denote the set of testing conditions, _C_ the set of all test cases, and _P_ the set of all participants. Each participant _i ∈ P_ completed a subset of test cases _Ci,k ⊆ C_ under condition _k ∈ K_ . For each test case _j_ under condition _k_ , let _Pj,k ⊆ P_ be the set of participants who took test case _j_ . The score achieved by participant _i_ on test case _j_ under condition _k_ is denoted by _Si,j,k_ , and _S_ max is the 

maximum possible score per test case. 

- _a) Accuracy per Participant and Condition:_ The accu- 

- racy _Ai,k_ for participant _i_ under condition _k_ is calculated as: 


![](images/Zhang_2025_Human_AI_Collaborative_Game_Testing_with_Vision_Language_Models.pdf-0005-09.png)


<!-- Start of picture text -->
� j∈Ci,k Si,j,k<br>Ai,k = (1)<br>|Ci,k| × S max<br><!-- End of picture text -->

_b) Average Accuracy per Condition:_ The average accuracy _A_<sup>¯</sup> _k_ for condition _k_ is: 


![](images/Zhang_2025_Human_AI_Collaborative_Game_Testing_with_Vision_Language_Models.pdf-0005-11.png)


<!-- Start of picture text -->
� i∈Pk � j∈Ci,k Si,j,k<br>A ¯ k = (2)<br>� i∈Pk |Ci,k| × S max<br><!-- End of picture text -->

where _Pk_ = _{i ∈ P | Ci,k̸_ = _∅}_ is the set of participants who completed any test cases under condition _k_ . 

_c) Accuracy per Test Case and Condition:_ The accuracy _Aj,k_ for test case _j_ under condition _k_ is: 


![](images/Zhang_2025_Human_AI_Collaborative_Game_Testing_with_Vision_Language_Models.pdf-0005-14.png)


<!-- Start of picture text -->
� i∈Pj,k Si,j,k<br>Aj,k = (3)<br>|Pj,k| × S max<br><!-- End of picture text -->

_d) Accuracy per Scenario and Condition:_ For a scenario _s_ (a set of test cases within a specific category), the accuracy _As,k_ under condition _k_ is: 


![](images/Zhang_2025_Human_AI_Collaborative_Game_Testing_with_Vision_Language_Models.pdf-0006-01.png)


<!-- Start of picture text -->
� j∈Cs � i∈Pj,k Si,j,k<br>As,k = (4)<br>� j∈Cs |Pj,k| × S max<br><!-- End of picture text -->

where _Cs ⊆ C_ is the set of test cases in scenario _s_ . 

_e) Explanation:_ This methodology accounts for varying numbers of participants per test case and condition. By aggregating scores and normalizing them with the appropriate maximum possible scores, we ensure accurate calculation of accuracy rates despite differences in participant assignments and test case distributions across conditions and scenarios. This allows for a comprehensive evaluation of performance across different testing conditions and scenarios. 

_3) Challenges Faced by Testers:_ Through participant interviews, we identified several issues that may have hindered accurate judgment during the testing process, and we have classified the challenging test cases as follows: 

- **Low Visibility (LV):** In low-visibility conditions, participants often struggle to identify potential graphical output errors, making defect detection challenging. This situation may lead to incorrect classifications as Lighting/Shadow Artifacts. 

- **Multiple Defects (MD):** Many game issues arise from the interplay of multiple defects, and participants may prioritize more apparent defects while overlooking others, leading to incomplete defect assessments. 

- **Subtle Defects (SD):** Subtle defects, such as missing structures indicated only by minimal hints or minor object misbehavior, are often overlooked or mistaken for normal occurrences, resulting in erroneous judgments. 

- **Ambiguous Boundaries (AB):** Different defect types may exhibit similar characteristics. For instance, scene loading errors in object consistency can sometimes resemble texture loss in graphical rendering errors, leading to misjudgments by participants. 

_4) Potential AI Errors:_ The output from the AI-assisted system is categorized into scene descriptions and defect assessments. During the testing process, we observed potential errors in the AI system that could influence participants’ results and classified test cases accordingly. The main types of errors include: 

- **Descriptive Errors (DE):** When the AI system inaccurately describes a game screenshot, participants may derive incorrect conclusions during defect analysis. 

- **Judgment Errors (JE):** Instances of misclassification in defect type recognition by the AI system may lead participants to rely excessively on the AI’s conclusions, resulting in erroneous judgments. 

- **Correct Description, Judgment Error (CDJE):** If the AI system accurately describes the scene but makes incorrect judgments, participants may trust the AI’s assessment and consequently make errors. This scenario 

frequently occurs when defect boundaries are unclear or when defects are non-unique. 

- **Both Description and Judgment Errors (DEJE):** When the AI system fails in both description and judgment, participants might correct erroneous judgments upon noticing discrepancies between the AI’s description and the visuals, or they may blindly trust the AI’s seemingly logical conclusions, leading to mistakes. 

_5) AI Hallucination Cases:_ AI hallucinations—when the system incorrectly detects defects—presented additional challenges for testers: 

- **False Negative Detections (FND):** In cases where defects were subtle or nuanced, the AI sometimes failed to detect any issues, incorrectly assessing the game visuals as defect-free. This mirrored the difficulty human testers experience in traditional testing, potentially leading to incomplete or inaccurate test reports. 

- **False Positive Detections (FPD):** When game visuals were highly stylized or contained elements that defied conventional design patterns (e.g., special effects or exaggerated color schemes), the AI frequently misidentified these as defects. Such misjudgments often occurred due to insufficient contextual information provided about the game’s design, causing the AI to flag intended artistic choices as errors. 

## IV. EXPERIMENT RESULTS AND ANALYSIS 

- _A. Summary of Key Findings_ 

The results of this study indicate that AI-assisted systems significantly enhance the effectiveness of human testers in identifying game defects, especially under challenging conditions. The integration of AI assistance with detailed knowledge of defects—including information generated by AI and access to game design documentation—yielded the highest effectiveness in bug detection. However, the study also uncovered unexpected patterns regarding the impact of AI errors and hallucinations on human decision-making, highlighting the complexities of human-AI collaboration in game testing. 

## _B. Comparison of Effectiveness Across Conditions_ 

To evaluate the impact of AI assistance and knowledge provision on defect detection accuracy, we compared participants’ performance across the four experimental conditions: Manual (M), Knowledge Assistance (KA), AI Assistance (AIA), and Knowledge plus AI Assistance (KA+AIA). As shown in Figure 3, AI assistance significantly improved defect detection accuracy. Specifically, participants in the AIA condition achieved an average accuracy of 62.7%, compared to 41.3% in the Manual condition—a statistically significant increase ( _p <_ 0 _._ 001). When AI assistance was combined with knowledge provision (KA+AIA), the average accuracy further increased to 64.4%. 

Interestingly, while knowledge provision alone (KA) improved average accuracy to 43.8% compared to the Manual condition, this difference was not statistically significant ( _p_ = 0 _._ 127). This suggests that AI assistance has a more substantial 


![](images/Zhang_2025_Human_AI_Collaborative_Game_Testing_with_Vision_Language_Models.pdf-0007-00.png)


<!-- Start of picture text -->
120<br>100<br>80<br>60<br>40<br>20<br>0<br>With AI Without AI<br>With Knowledge Without Knowledge<br>Accuracy (%)<br><!-- End of picture text -->

Fig. 3. Test accuracy distribution. This image illustrates the maximum, average, upper quartile, median, lower quartile, and minimum accuracies of participants under different testing conditions. 

effect on improving defect detection accuracy than knowledge provision alone. 

Furthermore, the interquartile range (IQR) for participants in the AI-assisted conditions was narrower than in the Manual and KA conditions, indicating more consistent performance among participants when AI assistance was provided. This consistency likely results from the AI system’s ability to reduce cognitive load by automating the detection of surfacelevel defects, allowing human testers to focus on more complex issues. 

These findings demonstrate that AI assistance significantly enhances human testers’ effectiveness in identifying game defects, and that combining AI assistance with detailed knowledge yields the highest accuracy. The results indicate the potential of AI to augment human capabilities in game testing, leading to more efficient and accurate defect detection processes. 

## _C. Impact of Gaming Experience on Testing Accuracy_ 

Participants without prior gaming experience showed a similar boost in accuracy from AI assistance, achieving 61.4% with AI and 45.7% without AI when no extra knowledge was provided (AIA vs. Manual). However, with the addition of knowledge, accuracy decreased to 59.3% with AI and 35.0% without AI (KA+AIA vs. KA). This suggests that while AI consistently improves accuracy, unfamiliarity with video games may make knowledge provision overwhelming, reducing effectiveness. Despite this, AI assistance helped this group achieve accuracy comparable to participants with prior gaming experience. 

Given the gaming scenario, we attracted few non-gamers. Due to the small sample size of 7 participants in this group, these findings are not statistically significant. Future work 

TABLE III 

ACCURACY OF AI-ASSISTED SYSTEMS UNDER CHALLENGING CONDITIONS 

||Manual (%)|AIA (%)|KA (%)|KA+AIA (%)|
|---|---|---|---|---|
|LV|42.4|71.6|47.0|65.3|
|MD|44.0|67.9|48.3|65.6|
|SD|36.6|54.7|46.5|62.3|
|AB|36.2|65.4|46.6|72.9|
|Others|41.3|62.9|43.0|64.5|



should involve a more diverse participant pool to better understand how gaming experience influences the effectiveness of AI and knowledge in game testing. 

_D. Accuracy of AI-Assisted Systems Under Challenging Scenarios_ 

To further assess the value of AI assistance, we analyzed participants’ accuracy in identifying defects under challenging conditions, such as low visibility (LV), multiple defects (MD), subtle defects (SD), and ambiguous boundaries (AB). Table III summarizes the accuracy across different conditions. 

_a) Low Visibility (LV):_ In low-visibility conditions, manual testers achieved an accuracy of 42.4%, indicating the difficulty of detecting defects when visibility is compromised. AI assistance substantially improved accuracy to 71.6% in the AIA condition ( _p <_ 0 _._ 001 compared to Manual), demonstrating AI’s effectiveness in processing visual information that may be challenging for humans. However, the KA+AIA condition saw a slightly lower accuracy of 65.3%, suggesting that additional knowledge may not significantly enhance performance in conjunction with AI assistance under lowvisibility conditions, possibly due to information overload or cognitive interference. 

_b) Multiple Defects (MD):_ When test cases contained multiple defects, manual testers achieved 44.0% accuracy. AI assistance again led to a significant improvement, with 67.9% accuracy in the AIA condition ( _p <_ 0 _._ 001). The KA+AIA condition achieved 65.6% accuracy, comparable to the AIA condition. This indicates that AI assistance helps testers manage the complexity of identifying multiple defects simultaneously, likely by systematically highlighting potential issues. 

_c) Subtle Defects (SD):_ Detecting subtle defects proved challenging for manual testers, with an accuracy of 36.6%. AI assistance improved accuracy to 54.7% in the AIA condition ( _p <_ 0 _._ 001), and further to 62.3% in the KA+AIA condition. The significant improvement in the condition KA + AIA suggests that the combination of AI assistance and detailed knowledge enables testers to detect subtle defects more effectively, perhaps by providing context that enhances the interpretation of AI output. 

_d) Ambiguous Boundaries (AB):_ In cases with ambiguous defect boundaries, manual testers had the lowest accuracy (36.2%). The AIA condition improved accuracy to 65.4% 

TABLE IV 

IMPACT OF AI ERROR INFORMATION ON HUMAN PARTICIPANTS 

||Manual (%)|AIA (%)|KA (%)|KA+AIA (%)|
|---|---|---|---|---|
|DE|41.5|35.2|38.2|44.5|
|JE|32.2|20.3|27.0|27.4|
|CDJE|37.0|51.7|25.5|54.6|
|DEJE|30.6|9.8|27.5|18.4|
|Others|41.3|68.0|45.5|68.5|



( _p <_ 0 _._ 001), while the KA+AIA condition achieved the highest accuracy of 72.9%. This substantial improvement indicates that when defects are difficult to classify, the combination of AI assistance and knowledge provision is particularly beneficial, likely because the detailed information helps testers resolve ambiguities in defect categorization. 

Overall, these results highlight that AI assistance significantly enhances defect detection accuracy under challenging conditions, and that the addition of knowledge provision can further improve performance in certain scenarios. The findings emphasize the importance of integrating AI tools with human expertise to address complex testing challenges effectively. 

## _E. Impact of AI Descriptive and Judgment Errors on Human Participants_ 

While AI assistance generally improved defect detection accuracy, it is crucial to understand how AI errors affect human testers. We analyzed the impact of AI descriptive errors (DE), judgment errors (JE), cases with correct description but judgment errors (CDJE), and cases with both description and judgment errors (DEJE) on participant accuracy. Table IV presents the accuracy across different conditions. 

_a) Descriptive Errors (DE)::_ In cases where the AI provided incorrect scene descriptions, participant accuracy decreased in the AIA condition (35.2%) compared to the Manual condition (41.5%). This suggests that misleading descriptions from the AI can negatively impact testers who rely on AI outputs. However, in the KA+AIA condition, accuracy improved to 44.5%, indicating that access to detailed knowledge helps participants identify and correct AI descriptive errors. 

_b) Judgment Errors (JE)::_ When the AI misclassified defects, participant accuracy was significantly lower in the AIA condition (20.3%) compared to the Manual condition (32.2%), highlighting the potential for AI judgment errors to mislead testers. The KA+AIA condition showed a slight improvement (27.4%), suggesting that knowledge provision partially mitigates the impact of AI judgment errors by enabling testers to critically assess AI outputs. 

_c) Correct Description, Judgment Error (CDJE)::_ In scenarios where the AI provided accurate descriptions but incorrect defect judgments, participants in the AIA condition achieved higher accuracy (51.7%) than in the Manual condition (37.0%). This implies that accurate descriptions allow testers to override incorrect AI judgments. The highest accuracy was observed in the KA+AIA condition (54.6%), 

TABLE V 

ACCURACY WHEN AI HALLUCINATES BUGS 

||Manual (%)|AIA (%)|KA (%)|KA+AIA (%)|
|---|---|---|---|---|
|FND|34.8|24.6|27.4|35.7|
|FPD|27.3|26.3|21.5|21.8|



reinforcing the benefit of combining AI assistance with knowledge provision. 

_d) Both Description and Judgment Errors (DEJE)::_ When the AI made both descriptive and judgment errors, participant accuracy was notably low in the AIA condition (9.8%), significantly lower than in the Manual condition (30.6%). This shows the detrimental effect of compounded AI errors on human performance. The KA+AIA condition showed some improvement (18.4%), indicating that knowledge provision can help testers identify and correct AI errors to some extent. 

These findings highlight that while AI assistance generally enhances performance, AI errors can adversely affect human testers, particularly when they rely heavily on AI outputs. Providing testers with additional knowledge and training to critically evaluate AI outputs is essential to mitigate the impact of AI errors. 

## _F. Impact of AI Hallucinations on Bug Detection_ 

AI hallucinations—instances where the AI incorrectly identifies defects in non-defective visuals or fails to detect actual defects—pose a significant challenge in AI-assisted game testing. We examined how AI hallucinations affected participant accuracy, focusing on false negative detections (FND) and false positive detections (FPD). Table V summarizes the results. 

_a) False Negative Detections (FND)::_ In cases where the AI failed to detect actual defects, participants in the AIA condition had lower accuracy (24.6%) compared to the Manual condition (34.8%). This indicates that reliance on AI can lead to missed defects when the AI overlooks issues. However, the KA+AIA condition showed an accuracy of 35.7%, similar to the Manual condition, suggesting that knowledge provision helps participants compensate for AI’s false negatives by relying on their own judgment informed by detailed information. 

_b) False Positive Detections (FPD)::_ When the AI incorrectly identified defects in non-defective visuals, participant accuracy was low across all conditions. The Manual condition achieved slightly higher accuracy (27.3%) compared to the AIA (26.3%) and KA+AIA (21.8%) conditions. This suggests that AI hallucinations of false positives can mislead testers, even when additional knowledge is provided. Participants may trust the AI’s assessment, especially if the AI presents plausible explanations for the supposed defects, leading to incorrect defect reports. 

## V. DISCUSSION 

In our analysis, one of the key outcomes is that participants utilizing AI assistance consistently achieved higher accuracy 

compared to those relying solely on manual testing. As shown in Table III, AI-assisted conditions (AIA and KA+AIA) led to substantial improvements in defect detection across scenarios with low visibility, multiple defects, subtle defects, and ambiguous boundaries. This demonstrates the potential of AI systems to augment human capabilities by efficiently handling surface-level defect detection, allowing testers to focus on more complex issues. 

However, the study also indicates that AI assistance is not infallible. AI errors—both descriptive and judgmental—negatively impacted human performance. When the AI provided incorrect descriptions or misclassified defects, participants’ accuracy decreased significantly in the AI-assisted conditions (Table IV). Moreover, AI hallucinations, where the AI incorrectly identified non-defective visuals as containing bugs or failed to detect actual defects, further misled testers (Table V). These findings align with existing literature on the risks of over-reliance on AI systems, where users may accept AI outputs without sufficient critical evaluation [22], [23]. 

Importantly, combining AI assistance with detailed knowledge provision (KA+AIA) mitigated some of the negative effects of AI errors. Participants with access to additional knowledge were better equipped to critically assess AI outputs, correct errors, and maintain higher accuracy levels, even when the AI made mistakes. For instance, in cases of correct description but judgment errors (CDJE), the KA+AIA condition achieved the highest accuracy (54.6%), indicating that knowledge provision helps testers override incorrect AI judgments (Table IV). This emphasizes the crucial role of human oversight and the value of equipping testers with sufficient context to make informed decisions. 

The study also reveals that while knowledge provision alone (KA) did not significantly improve accuracy compared to manual testing, its combination with AI assistance led to the highest performance. This suggests that AI assistance enhances human performance most effectively when testers are supported by both AI tools and adequate knowledge resources. However, there is a need to balance the amount of information provided to avoid cognitive overload, which can hinder decision-making efficiency [54], [55]. 

Our findings highlight the importance of designing AI systems that are not only accurate but also transparent and interpretable, enabling testers to understand and critically evaluate AI outputs. Additionally, training testers to maintain a critical perspective towards AI assistance and to effectively use the provided knowledge resources is essential to maximize the benefits of AI integration. 

## VI. CONCLUSION 

Through a comprehensive user study, we demonstrated that AI assistance significantly enhances real-world human testers’ effectiveness in identifying game defects, particularly when combined with detailed knowledge resources. By integrating AI-driven defect detection with human oversight, we experimented a hybrid testing workflow that optimizes efficiency and accuracy in game testing processes. 

However, the research also highlights challenges associated with AI errors and hallucinations, which can negatively impact performance if not properly managed. These findings emphasize the critical need for effective human-AI collaboration, where testers are equipped to critically assess and correct AI outputs. Developing improved collaborative frameworks and interaction models is essential to address the problems associated with AI errors and to facilitate better and easier human judgment. 

Our study contributes to the understanding of human-AI interaction in complex decision-making environments, revealing the dual role of AI as both an enhancer and a potential source of error in game testing. Practically, the study suggests that providing testers with manageable knowledge resources and training in critical evaluation can maximize the benefits of AI assistance while mitigating risks. 

Limitations of this study include a participant pool with predominantly gaming experience, which may affect generalizability, and a focus on specific defect types and testing conditions. Future research should include a more diverse range of participants and expand the scope to various game genres and complex scenarios. Additionally, improving AI transparency and developing strategies to enhance human oversight will be crucial for advancing AI-assisted game testing methodologies. 

In conclusion, by addressing the identified challenges and fostering effective human-AI collaboration, the gaming industry can leverage AI to achieve more efficient, accurate, and reliable testing processes. 

## REFERENCES 

- [1] L. Levy and J. Novak, _Game development essentials: Game QA & testing_ . Delmar Learning, 2009. 

- [2] P. Barr, J. Noble, and R. Biddle, “Video game values: Human–computer interaction and games,” _Interacting with computers_ , vol. 19, no. 2, pp. 180–195, 2007. 

- [3] X. Liang, J. Qi, Y. Gao, C. Peng, and P. Yang, “Ag3: Automated game gui text glitch detection based on computer vision,” in _Proceedings of the 31st ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering_ , 2023, pp. 1879–1890. 

- [4] J. Chueca, J. Ver´on, J. Font, F. P´erez, and C. Cetina, “The consolidation of game software engineering: A systematic literature review of software engineering for industry-scale computer games,” _Information and Software Technology_ , vol. 165, p. 107330, 2024. 

- [5] C. Politowski, F. Petrillo, and Y.-G. Gu´eh´eneuc, “A survey of video game testing,” in _2021 IEEE/ACM International Conference on Automation of Software Test (AST)_ . IEEE, 2021, pp. 90–99. 

- [6] J. Pfau, J. D. Smeddinck, and R. Malaka, “Automated game testing with icarus: Intelligent completion of adventure riddles via unsupervised solving,” in _Extended abstracts publication of the annual symposium on computer-human interaction in play_ , 2017, pp. 153–164. 

- [7] S. Rahman, A. Baz, S. Misailovic, and A. Shi, “Quantizing largelanguage models for predicting flaky tests,” in _2024 IEEE Conference on Software Testing, Verification and Validation (ICST)_ . IEEE, 2024, pp. 93–104. 

- [8] P. Dhavachelvan, G. Uma, and V. Venkatachalapathy, “A new approach in development of distributed framework for automated software testing using agents,” _Knowledge-Based Systems_ , vol. 19, no. 4, pp. 235–247, 2006. 

- [9] R. Ramadan and B. Hendradjaya, “Development of game testing method for measuring game quality,” in _2014 International Conference on Data and Software Engineering (ICODSE)_ . IEEE, 2014, pp. 1–6. 

- [10] M. R. Taesiri, M. Habibi, and M. A. Fazli, “A video game testing method utilizing deep learning,” _Iran Journal of Computer Science_ , vol. 17, no. 2, 2020. 

- [11] V. H. Durelli, R. S. Durelli, S. S. Borges, A. T. Endo, M. M. Eler, D. R. Dias, and M. P. Guimar˜aes, “Machine learning applied to software testing: A systematic mapping study,” _IEEE Transactions on Reliability_ , vol. 68, no. 3, pp. 1189–1212, 2019. 

- [12] C. Paduraru, M. Paduraru, and A. Stefanescu, “Automated game testing using computer vision methods,” in _2021 36th IEEE/ACM International Conference on Automated Software Engineering Workshops (ASEW)_ . IEEE, 2021, pp. 65–72. 

- [13] E. Azizi and L. Zaman, “Astrobug: Automatic game bug detection using deep learning,” _IEEE Transactions on Games_ , 2024. 

- [14] C. Paduraru, M. Cernat, and A. Stefanescu, “Automated evaluation of game content display using deep learning,” in _Proceedings of the 28th International Conference on Evaluation and Assessment in Software Engineering_ , 2024, pp. 421–424. 

- [15] G. Liu, M. Cai, L. Zhao, T. Qin, A. Brown, J. Bischoff, and T.-Y. Liu, “Inspector: Pixel-based automated game testing via exploration, detection, and investigation,” in _2022 IEEE Conference on Games (CoG)_ . IEEE, 2022, pp. 237–244. 

- [16] A. Senchenko, N. Patterson, H. Samuel, and D. Ispir, “Supernova: Automating test selection and defect prevention in aaa video games using risk based testing and machine learning,” in _2022 IEEE Conference on Software Testing, Verification and Validation (ICST)_ . IEEE, 2022, pp. 345–354. 

- [17] A. Arcuri, “Restful api automated test case generation,” in _2017 IEEE International Conference on Software Quality, Reliability and Security (QRS)_ . IEEE, 2017, pp. 9–20. 

- [18] S. Ariyurek, A. Betin-Can, and E. Surer, “Automated video game testing using synthetic and humanlike agents,” _IEEE Transactions on Games_ , vol. 13, no. 1, pp. 50–67, 2019. 

- [19] Y. K. Dwivedi, L. Hughes, E. Ismagilova, G. Aarts, C. Coombs, T. Crick, Y. Duan, R. Dwivedi, J. Edwards, A. Eirug _et al._ , “Artificial intelligence (ai): Multidisciplinary perspectives on emerging challenges, opportunities, and agenda for research, practice and policy,” _International journal of information management_ , vol. 57, p. 101994, 2021. 

- [20] F. Cabitza, C. Fregosi, A. Campagner, and C. Natali, “Explanations considered harmful: The impact of misleading explanations on accuracy in hybrid human-ai decision making,” in _World Conference on Explainable Artificial Intelligence_ . Springer, 2024, pp. 255–269. 

- [21] W. Xu, M. J. Dainoff, L. Ge, and Z. Gao, “From human-computer interaction to human-ai interaction: new challenges and opportunities for enabling human-centered ai,” _arXiv preprint arXiv:2105.05424_ , vol. 5, 2021. 

- [22] V. Rawte, A. Sheth, and A. Das, “A survey of hallucination in large foundation models,” _arXiv preprint arXiv:2309.05922_ , 2023. 

- [23] Y. Zhang, Y. Li, L. Cui, D. Cai, L. Liu, T. Fu, X. Huang, E. Zhao, Y. Zhang, Y. Chen _et al._ , “Siren’s song in the ai ocean: a survey on hallucination in large language models,” _arXiv preprint arXiv:2309.01219_ , 2023. 

- [24] W. Sun, Z. Shi, S. Gao, P. Ren, M. de Rijke, and Z. Ren, “Contrastive learning reduces hallucination in conversations,” in _Proceedings of the AAAI Conference on Artificial Intelligence_ , vol. 37, no. 11, 2023, pp. 13 618–13 626. 

- [25] X. Chen, L. Wang, W. Wu, Q. Tang, and Y. Liu, “Honest ai: Finetuning” small” language models to say” i don’t know”, and reducing hallucination in rag,” in _2024 KDD Cup Workshop for Retrieval Augmented Generation_ , 2024. 

- [26] S. N. Stahlke and P. Mirza-Babaei, “Usertesting without the user: Opportunities and challenges of an ai-driven approach in games user research,” _Computers in Entertainment (CIE)_ , vol. 16, no. 2, pp. 1–18, 2018. 

- [27] S. Jintawatsakoon, “Visual glitches classification for video game using deep learning-based techniques,” in _2023 27th International Computer Science and Engineering Conference (ICSEC)_ . IEEE, 2023, pp. 116– 121. 

- [28] A. Sestini, L. Gissl´en, J. Bergdahl, K. Tollmar, and A. D. Bagdanov, “Automated gameplay testing and validation with curiosity-conditioned proximal trajectories,” _IEEE Transactions on Games_ , vol. 16, no. 1, pp. 113–126, 2022. 

- [29] G. Meszaros, _xUnit test patterns: Refactoring test code_ . Pearson Education, 2007. 

- [30] OpenAI, “Gpt-4o: Openai platform documentation,” 2024, accessed: 2024-09-30. [Online]. Available: https://platform.openai.com/docs/models/gpt-4o 

- [31] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image recognition,” in _Proceedings of the IEEE conference on computer vision and pattern recognition_ , 2016, pp. 770–778. 

- [32] A. Krizhevsky, I. Sutskever, and G. E. Hinton, “Imagenet classification with deep convolutional neural networks,” _Communications of the ACM_ , vol. 60, no. 6, pp. 84–90, 2017. 

- [33] I. Prasetya, F. Pastor Ric´os, F. M. Kifetew, D. Prandi, S. Shirzadehhajimahmood, T. E. Vos, P. Paska, K. Hovorka, R. Ferdous, A. Susi _et al._ , “An agent-based approach to automated game testing: an experience report,” in _Proceedings of the 13th International Workshop on Automating Test Case Design, Selection and Evaluation_ , 2022, pp. 1–8. 

- [34] K. Chen, Y. Li, Y. Chen, C. Fan, Z. Hu, and W. Yang, “Glib: towards automated test oracle for graphically-rich applications,” in _Proceedings of the 29th ACM Joint Meeting on European Software Engineering Conference and Symposium on the Foundations of Software Engineering_ , 2021, pp. 1093–1104. 

- [35] D. Norman, _The design of everyday things: Revised and expanded edition_ . Basic books, 2013. 

- [36] B. Shneiderman, C. Plaisant, M. S. Cohen, S. Jacobs, N. Elmqvist, and N. Diakopoulos, _Designing the User Interface: Strategies for Effective Human-Computer Interaction_ . Pearson, 2016. 

- [37] A. Dix, _Human-computer interaction_ . Pearson Education, 2004. 

- [38] R. Hartson and P. S. Pyla, _The UX book: Agile UX design for a quality user experience_ . Morgan Kaufmann, 2018. 

- [39] J. Lazar, J. H. Feng, and H. Hochheiser, _Research methods in humancomputer interaction_ . Morgan Kaufmann, 2017. 

- [40] K. Vodrahalli, T. Gerstenberg, and J. Y. Zou, “Uncalibrated models can improve human-ai collaboration,” _Advances in Neural Information Processing Systems_ , vol. 35, pp. 4004–4016, 2022. 

- [41] T. Boyacı, C. Canyakmaz, and F. de V´ericourt, “Human and machine: The impact of machine input on decision making under cognitive limitations,” _Management Science_ , vol. 70, no. 2, pp. 1258–1275, 2024. 

- [42] B. Gebru, L. Zeleke, D. Blankson, M. Nabil, S. Nateghi, A. Homaifar, and E. Tunstel, “A review on human–machine trust evaluation: Human-centric and machine-centric perspectives,” _IEEE Transactions on Human-Machine Systems_ , vol. 52, no. 5, pp. 952–962, 2022. 

- [43] Z. Zhang, J. Singh, U. Gadiraju, and A. Anand, “Dissonance between human and machine understanding,” _Proceedings of the ACM on HumanComputer Interaction_ , vol. 3, no. CSCW, pp. 1–23, 2019. 

- [44] P. Harms, “Automated usability evaluation of virtual reality applications,” _ACM Transactions on Computer-Human Interaction (TOCHI)_ , vol. 26, no. 3, pp. 1–36, 2019. 

- [45] S. Varvaressos, K. Lavoie, S. Gaboury, and S. Hall´e, “Automated bug finding in video games: A case study for runtime monitoring,” _Computers in Entertainment (CIE)_ , vol. 15, no. 1, pp. 1–28, 2017. 

- [46] G. Rani, U. Pandey, A. A. Wagde, and V. S. Dhaka, “A deep reinforcement learning technique for bug detection in video games,” _International Journal of Information Technology_ , vol. 15, no. 1, pp. 355–367, 2023. 

- [47] A. Albaghajati and M. Ahmed, “Video game automated testing approaches: An assessment framework,” _IEEE transactions on games_ , vol. 15, no. 1, pp. 81–94, 2020. 

- [48] A. Nantes, R. Brown, and F. Maire, “A framework for the semi-automatic testing of video games,” in _Proceedings of the AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment_ , vol. 4, no. 1, 2008, pp. 197–202. 

- [49] C. Paduraru, M. Paduraru, and A. Stefanescu, “Rivergame-a game testing tool using artificial intelligence,” in _2022 IEEE Conference on Software Testing, Verification and Validation (ICST)_ . IEEE, 2022, pp. 422–432. 

- [50] N. Ballou, A. Denisova, R. Ryan, C. S. Rigby, and S. Deterding, “The basic needs in games scale (bangs): A new tool for investigating positive and negative video game experiences,” _International Journal of HumanComputer Studies_ , vol. 188, p. 103289, 2024. 

- [51] C. P. Schultz and R. D. Bryant, _Game testing: All in one_ . Mercury Learning and Information, 2016. 

- [52] R. Coppola, T. Fulcini, and F. Strada, “Know your bugs: A survey of issues in automated game testing literature,” in _2024 IEEE Gaming, Entertainment, and Media Conference (GEM)_ . IEEE, 2024, pp. 1–6. 

- [53] B. Jiang, W. Wei, L. Yi, and W. Chan, “Droidgamer: Android game testing with operable widget recognition by deep learning,” in _2021 IEEE 21st International Conference on Software Quality, Reliability and Security (QRS)_ . IEEE, 2021, pp. 197–206. 

- [54] M. Andrejevic, _Infoglut: How too much information is changing the way we think and know_ . Routledge, 2013. 

[55] A. Zou, W. Yu, H. Zhang, K. Ma, D. Cai, Z. Zhang, H. Zhao, and D. Yu, “Docbench: A benchmark for evaluating llm-based document reading systems,” _arXiv preprint arXiv:2407.10701_ , 2024. 

