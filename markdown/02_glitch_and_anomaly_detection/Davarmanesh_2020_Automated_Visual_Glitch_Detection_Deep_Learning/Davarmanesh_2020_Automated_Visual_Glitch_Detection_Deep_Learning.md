# **Discretization-Aware Architecture Search** 

Yunjie Tian<sup>1</sup> , Chang Liu<sup>1</sup> , Lingxi Xie<sup>2</sup> , Jianbin Jiao<sup>1</sup> , Qixiang Ye<sup>1</sup> 

> 1 University of Chinese Academy of Sciences, 

> 2 Noahs Ark Lab, Huawei 

**Abstract.** The search cost of neural architecture search (NAS) has been largely reduced by weight-sharing methods. These methods optimize a super-network with all possible edges and operations, and determine the optimal sub-network by discretization, _i.e._ , pruning off weak candidates. The discretization process, performed on either operations or edges, incurs significant inaccuracy and thus the quality of the final architecture is not guaranteed. This paper presents discretization-aware architecture search (DA<sup>2</sup> S), with the core idea being adding a loss term to push the super-network towards the configuration of desired topology, so that the accuracy loss brought by discretization is largely alleviated. Experiments on standard image classification benchmarks demonstrate the superiority of our approach, in particular, under imbalanced target network configurations that were not studied before. The code is available at https://github.com/sunsmarterjie/DAAS. 

**Keywords:** Neural Architecture Search, Weight-Sharing, Discretization Gap, Discretization-Aware. 

## **1 Introduction** 

Network architecture search (NAS) is a research topic aimming to explore the design of neural networks in a large space that is not well covered by human expertise. To alleviate the computational burden of the reinforcement-based [1,2] and evolutionary [3,4,5] algorithms that evaluate sampled architecture individually, researchers proposed one-shot search methods [6] which first optimized a super-network with all possible architectures included, and then sampled subnetworks from it for evaluation [7]. By sharing computation, this kind of methods accelerated NAS by 3–4 orders of magnitudes. 

A representative example of one-shot search is differentiable architecture search (DARTS [8]), which formulates the super-network into a differentiable form with respect to a set of architectural parameters, _e.g._ , operations and connections, so that the entire NAS process can be optimized in an end-to-end manner. DARTS did not require an explicit process for evaluating each subnetwork, but performed a standalone discretization process to determine the optimal sub-architecture, on which re-training is performed. Such an efficient search strategy does not require the search cost to increase dramatically as the size of search space, and the space can be much larger compared with other NAS approaches. 

Yunjie Tian, Chang Liu, Lingxi Xie, Jianbin Jiao, Qixiang Ye 

2 


![](images/Davarmanesh_2020_Automated_Visual_Glitch_Detection_Deep_Learning.pdf-0002-02.png)


<!-- Start of picture text -->
0 1 0 1 2 0.182 0 1 0 1 DARTS (acc. %)<br>0.243<br>… … … 0.1240.135 6 /𝟏𝟒 8 /𝟏𝟒<br>2 3 + + + 2 3 2 3 searched 87.87 87.87<br>3 discretizated 9.96 10.34<br>4 5 Search & Discretization 4 5 4 5 retrained 97.07 97.22<br>𝐃𝐀𝐑𝐓𝐒 8 /𝟏𝟒 6 /𝟏𝟒<br>0 1 0 1 2 0.9820.003 0 1 DA 2 S (acc. %)<br>… … … 0.0020.003 6 /𝟏𝟒 8 /𝟏𝟒<br>2, 1 2 3 2, 1 + + + 0.495 2 3 searched 84.29 84.93<br>3 0.491 discretizated 64.24 67.11<br>2, 1 4 5 2, 1 Discretization-aware Search 4 5 retrained 97.35 97.47<br>𝐃𝐀 𝟐 𝐒 8 /𝟏𝟒<br>0 1 0 … 1… …2 0.0040.0030.0020.985 0 1 𝐦𝐚𝐱_𝐩𝐨𝐨𝐥𝑚, 𝑛 𝑒𝑎𝑐ℎ𝑐𝑜𝑛𝑡𝑎𝑖𝑛𝑠𝒏𝑜𝑝𝑒𝑟𝑎𝑡𝑖𝑜𝑛𝑠𝑛𝑜𝑑𝑒𝑤𝑖𝑡ℎ𝒎𝑖𝑛𝑝𝑢𝑡𝑒𝑑𝑔𝑒𝑠,𝐬𝐤𝐢𝐩_𝐜𝐨𝐧𝐧𝐞𝐜𝐭<br>1, 1 2 3 1, 1 + + + 0.992 2 3 𝐬𝐞𝐩_𝐜𝐨𝐧𝐯_𝟓× 𝟓 𝐝𝐢𝐥_𝐜𝐨𝐧𝐯_𝟑× 𝟑<br>3<br>𝐬𝐞𝐩_𝐜𝐨𝐧𝐯_𝟑× 𝟑 𝐝𝐢𝐥_𝐜𝐨𝐧𝐯_𝟓× 𝟓<br>2, 1 4 5 2, 1 Discretization-aware Search 4 5 𝐚𝐯𝐠_𝐩𝐨𝐨𝐥<br>𝐃𝐀 𝟐 𝐒 6 /𝟏𝟒<br><!-- End of picture text -->

Fig. 1: **Top** : the normal cell of DARTS, from which we investigate node3 which sums up 3 input edges in the search stage. In two discretization configurations (preserving 8 and 6 out of 14 edges), this node can preserve 2 and 1 input(s), respectively, but pruning off inputs with moderate weights can lead to dramatic super-network accuracy and unsatisfying re-training accuracy. **Middle & Bottom** : DA<sup>2</sup> S is aware of the number of inputs to be preserved for each node and pushes weights to get close to either 1 or 0, so as the discretization loss is largely alleviated, and re-training accuracy improved. This figure is best viewed in color. 

Despite of the superiority about efficiency, DARTS is believed to suffer the gap between the optimized super-network and the sampled sub-networks. In particular, as illustrated in [9], the difference between the number of cells can cause a ‘depth gap’, and the search performance is largely stabilized by alleviating the gap. In this paper, we point out another gap, potentially more important, caused by the process of discretizing architectural weights of the super-network. To be specific, DARTS combines candidate operations and edges with a weighted sum (the weights are learnable), and preserves a fixed number of candidates with strong weights and discards others. However, there is no guarantee that the discarded weights are relatively small – if not, this discretization process can introduce significant inaccuracy in neural responses to **each** cell. Such inaccuracy accumulates and finally causes that **a well-optimized super-network does not necessarily generates high-quality sub-networks** , in particular (i) when the the discarded candidates still have moderate weights; and/or (ii) the number of pruned edges is relatively small compared to that in the super-network. Figure 1 shows a cell optimized by DARTS. One can see that discretization causes the super-network accuracy to drop dramatically, which also harms the performance of searched architecture in the re-training stage. 

Discretization-Aware Architecture Search 3 

To alleviate the above issue, we propose discretization-aware architecture search (DA<sup>2</sup> S). The main idea is to introduce an additional term to the loss function, so that the architectural parameters of the super-network is gradually pushed towards the desired configuration during the search process. To be specific, we formulate the new loss term into an entropy function based on the property that minimizing the entropy of a system drives maximizing the sparsity and discretization of the elements (weights) in the system. The objective of entropy is to enforce each weight to get close to either 0 or 1, with the number of 1’s determined by the desired configuration, so that the discretization process, by removing candidates with weights close to 0, does not incur significant accuracy loss. Being differentiable to architectural parameters, the entropy function can be freely plugged into the system for SGD optimization. We perform experiments on two standard image classification benchmarks, namely, CIFAR10 and ImageNet, based on PC-DARTS [10], an efficient variant of DARTS. Note that two sets of architectural parameters exist in PC-DARTS, taking control of operations in an edge and edges that sum into a node, respectively, and they are potentially equipped with different loss terms. We evaluate different configurations ( _i.e._ , varying from each other in the number of preserved edges for each node), most of which have not been studied before. When each search process reaches the end, the super-network converges into a discretization-friendly form, and the discretization process causes much smaller accuracy drop than that reported without the entropy loss. Consequently, the searched architecture, under any configuration, enjoys higher yet more stable performance, and the advantage is more significant as the configuration becomes more imbalanced, on which the original search method suffers a larger ‘discretization gap’. 

## **2 Related Work** 

The rapid development of deep learning [11], in particular convolutional neural networks, have largely changed the way of designing computational models in computer vision. Recent years have witnessed a trend of stacking more and more convolutional layers to a deep network [12,13,14,15] so that more trainable parameters are included and higher recognition accuracy is achieved. 

Going one step further, researchers started to consider the possibility that designs deep networks automatically, and thereby created a new research area termed neural architecture search (NAS) [1]. NAS defines a sub-field of automated machine learning (AutoML) [16] and has attracted increasing attentions in both academia and industry. The idea is to construct a sufficiently large space and thus enables the architecture to adjust according to training data, simulating the process of evolutionary computation. With carefully monitored search strategies, NAS has claimed better performance compared to hand-designed networks in a wide range of applications including image classification [1], object detection [17], and semantic segmentation [18]. 

The early efforts of NAS mainly involved heuristic search in a very large space, and the sampled architectures were often evaluated individually. Repre- 

4 Yunjie Tian, Chang Liu, Lingxi Xie, Jianbin Jiao, Qixiang Ye 

sentative examples include using reinforcement learning (RL) to formulate network or block designs [1,2,19], applying evolutionary algorithms (EA) to force the network evolve throughout iterations [3,4], or simply performing guided random search to find competitive solutions [5]. These methods often require a vast amount of computation, _e.g._ , thousands of GPU-days. To accelerate the search process, one-shot architecture search was proposed to share computation among architectures with similar building blocks [6]. 

One-shot architecture search was later developed into weight-reusing [20] and weight-sharing [7] methods which can reduce the search costs by orders of magnitudes. Beyond this point, researchers proposed to improve the search stability using better sampling methods [21,22], explored the importance of the search space [23], and tried to integrate hardware consumption such as latency as additional evaluation metrics [24]. These efforts eventually leads to powerful architectures that achieve state-of-the-art performance on ImageNet [20] with moderate computational cost overhead. 

A special family of one-shot architecture search falls into formulating the search space into a super-network which can adjust itself in a continuous space [25]. Based on this, the network and architectural parameters can be jointly optimized, which leads to a differentiable approach for architecture search. DARTS [8], a representative differentiable framework, designed an over-parameterized supernetwork which contains exponentially many sub-networks with shared weights. It performed bi-level optimization to update network weights and architectural weights alternately and, at the end of the search stage, used a greedy algorithm to prune off the operations and edges with lower weights. Partially-Connected DARTS [10] pursed a more efficient search by sampling a small part of supernetwork to reduce the redundancy in exploring the network space. 

Recent DARTS methods [9,10] have achieved success on both architecture quality and search efficiency. Nevertheless few researchers noticed that the discretization process incurs a significant accuracy loss, which makes it difficult to obtain a high-quality sub-network from the optimal sub-network [26]. This paper investigates this problem born with DARTS methods in a systematic way with the target to search discretization-aware architectures from the perspective of model regularization. 

## **3 Discretization-Aware Architecture Search** 

### **3.1 Preliminaries: DARTS** 

DARTS [8] designs a cell-based search space to facilitate efficient differentiable architecture search. Each cell is represented as a directed acyclic graph with _N_ nodes, where each node defines a network layer. There is a pre-defined space of operations denoted by _O_ , where each element, _o_ ( _·_ ), denotes a fixed operation. Commonly used operations include identity connection, and 3 _×_ 3 convolution performed at a network layer. 

Within a cell, the searching goal is to choose one operation from _O_ for each pair of nodes. Let ( _i, j_ ) denote a pair of nodes, where 0 ⩽ _i < j_ ⩽ _N −_ 1. The 

Discretization-Aware Architecture Search 5 

primary idea of DARTS is to formulate the information and gradient propagated from _i_ to _j_ as a weighted sum over _|O|_ operations, as _fi,j_ ( **z** _i_ ) =<sup>�</sup> _o∈O_<sup>_ao_</sup> _i,j_<sup>_· o_(</sup><sup>**z**</sup><sup>_i_),</sup> exp _<u>{α</u>_<sup>_o_</sup> _i,j_<sup>_<u>}</u>_</sup> where _a_<sup>_o_</sup> _i,j_<sup>=</sup> <u>�</u> _o_<sup>_′_</sup> _∈O_<sup>exp</sup><sup>_{αo_</sup> _i,j_<sup>_<u>′</u>}_and</sup><sup>**z**</sup><sup>_i_denotestheoutputofthe</sup><sup>_i_-thnode,and</sup><sup>**_α_**</sup> is a set of architectural parameters to weight operations within each edge, with _αi,j_<sup>_o_determiningtheweightof</sup><sup>_o_(</sup><sup>_·_)inedge(</sup><sup>_i, j_).FollowingPC-DARTS[10],we</sup> introduce an extra set of architectural parameters ( **_β_** ) in our DA<sup>2</sup> S to determine the weight of each edge. Thus, the output of a node is the sum of all input flows, _i.e._ , **z** _j_ =<sup>�</sup> _i<j_<sup>_bi,j· fi,j_(</sup><sup>**z**</sup><sup>_i_),where</sup><sup>_bi,j_=</sup> <u>�</u> _i_<sup>_′_</sup> _<j_ exp<sup>exp</sup> _<u>{βi</u>_<sup>_{_</sup> _<u>,j</u>_<sup>_β_</sup> _<u>}i</u>_<sup>_′_</sup> _,j_<sup>_}_.Theoutputof</sup> the entire cell is formed by concatenating the output of all prior nodes, _i.e._ , concat( **z** 2 _,_ **z** 3 _, . . . ,_ **z** _N −_ 1). Note that the first two nodes, **z** 0 and **z** 1, are input nodes to a cell, which are fixed during the search procedure. 

This design makes the entire framework differentiable to both layer weights and hyper-parameters _αi,j_<sup>_o_,sothatitispossibletoperformarchitecturesearch</sup> in an end-to-end fashion. After the search process is completed, on each edge ( _i, j_ ), the operation _o_ with the largest _αi,j_<sup>_o_valueispreserved,andeachnode</sup> _j_ is connected to two precedents _i < j_ with the largest _αi,j_<sup>_o_preserved.Denote</sup> the architectural parameters as **_α_** = _{αi,j_<sup>_o}_,andtheoverallsuper-networkas</sup> _F_ **_α_** _,_ **_θ_** ( _·_ ), which is parameterized by both **_α_** and **_θ_** ( **_α_** ). The learning procedure of DARTS optimizes the image classification loss to determine **_α_** and **_θ_** , as 


![](images/Davarmanesh_2020_Automated_Visual_Glitch_Detection_Deep_Learning.pdf-0005-03.png)


<!-- Start of picture text -->
M<br>arg min α , θ L C( α ,  θ ) = M 1 � y m ⊤ ·  log � F α , θ ( x m )� , (1)<br>m =1<br><!-- End of picture text -->

where _{_ **x** _m,_ **y** _m}_<sup>_M_</sup> _m_ =1<sup>denotesabatchoftrainingsampleswithcorresponding</sup> class labels. 

### **3.2 The Devil is in the Discretization Loss** 

It is well acknowledged that DARTS-based approaches suffer limited stability, _i.e._ , when the same search procedure runs for several times individually, the searched architectures can report varying performance during the re-training stage. For this reason, the original DARTS [8] evaluated the architectures found in four individual search phases on the validation set and picked up the best one, which results in 4 _×_ search cost. More importantly, as the search space gets enlarged, the number of trials require to find a high-quality architecture may also increase, and finally, the DARTS-based approaches may lose the advantage in efficiency. 

An important insight that our work delivers is that the instability is partly caused by the discretization loss. Here, by discretization we mean the process that picks up the best operation and/or edge and discards others according to the architectural weights of the super-network, _i.e._ , the continuous parameters, **_α_** and **_β_** , are discretized so that a pre-defined number of elements are optimized towards 1 and others close to 0. This obviously introduces inaccuracy to the welltrained super-network. To show this, we follow DARTS to train a super-network 

6 Yunjie Tian, Chang Liu, Lingxi Xie, Jianbin Jiao, Qixiang Ye 

on CIFAR10, which reports an accuracy of 87 _._ 87% on the validation set. Then, we investigate the impact of discretization by replacing the corresponding part with the trained weights, _e.g._ , on each edge, keeping the dominating operation (using a weight of 1) with its parameters ( _e.g._ , convolutional weights) unchanged. Results are shown in Figure 1. The accuracy drop is dramatic, _e.g._ , under the setting of DARTS (each node has 2 edges preserved), the validation accuracy drops from 87 _._ 87% to 10 _._ 34%. If we investigate a more imbalanced discretization (the first two nodes have 1 edge each and the last two nodes have 2 edges each), the validation accuracy drops to 9 _._ 96%, which is even close to a random guess. This is unexpected and violates the design nature of one-shot NAS, which suggests that dramatically bad sub-networks can be sampled from a well-trained supernetwork. Consequently, there is no guarantee that architectures found in this way can eventually report good performance, even after a complete re-training process has been performed. 

We argue that such gap is caused by that the training process is not aware of that a discretization process will be performed afterwards. For example, when _|O|_ operations are competing in an edge ( _i, j_ ), they ‘assume’ that the input, **x** _i_ is a weighted sum of the outputs of all nodes prior to _i_ . When discretization is performed, **x** _i_ is modified into the output of the dominating node, but the weights on edge ( _i, j_ ) may not match the new input. Such inaccuracy accumulates throughout the entire network and eventually leads to catastrophic accuracy drop. Therefore, the key to alleviate the gap is to make the search process aware of discretization, as well as the topology of the final architecture. We will elaborate our solution in the next part. 

### **3.3 Entropy-based Discretization-Aware Search** 

Figure 2 shows the overall framework of discretization-aware search. The main idea is to use the topology constraint to guide the optimization process, so that super-network eventually gets close to a sub-network that is allowed to appear as the final architecture. This is achieved by adding a loss function that measures the minimal distance between the current super-network and any acceptable sub-network. Specifically, we introduce an entropy-based loss function for each set of architectural parameters to fulfil this goal. 

Below we elaborate the details when applying this methodology to two sets of parameters, **_α_** (operation) and **_β_** (edge), followed by discussions on the priority of discretization and the relationship between prior works and our DA<sup>2</sup> S. 

### _•_ **Discretization of** **_α_ and** **_β_** 

We start with discretizing **_α_** . To guarantee that only one operation dominates on each edge when the search process ends, we compute the following loss for each edge ( _i, j_ ): 


![](images/Davarmanesh_2020_Automated_Visual_Glitch_Detection_Deep_Learning.pdf-0006-08.png)


<!-- Start of picture text -->
L O i,j ( α ) =  − o � ∈O � o ′ exp ∈O exp � αi o ,j � α � i,j o′ � ·  log � o ′ exp ∈O exp � αi o ,j � α � i,j o′ � . (2)<br><!-- End of picture text -->

Discretization-Aware Architecture Search 

7 


![](images/Davarmanesh_2020_Automated_Visual_Glitch_Detection_Deep_Learning.pdf-0007-02.png)


<!-- Start of picture text -->
Operation(α) Discretization<br>𝑎𝑖𝑗𝑘 = σ𝑜’𝜖𝒪𝑒𝑥𝑝(𝛼𝑒𝑥𝑝(𝛼𝑖𝑜𝑘,𝑗 )𝑖,𝑗𝑜’ ) 𝑎𝑎𝑎030031032 0.1250.1250.125 0.350 0.1050.015 0.0050.005<br>0 𝑎𝑎030334 0.1250.125 0.125 0.900 0<br>𝑎035 0.125 0.200<br>1 𝑎𝑎036037 0.1250.125 0.0550.0950.055 0.0540.0200.0030.0070.006 1<br>在此处键入公式。 𝐿 =  𝐿 𝐶 +         + 𝐿 𝑂 𝐿 𝐸 Searching  Procedure<br>2 2<br>𝑏03 0.33 0.40 0.50<br>𝑏13 0.33 0.25 0.05<br>3 𝑏𝑖𝑗 = σ𝑖’<𝑗𝑒𝑥𝑝(𝛽𝑒𝑥𝑝(𝛽𝑖,𝑗)𝑖’,𝑗) 𝑏23 0.33 0.35 0.45 3<br>Edge (β) Discretization<br><!-- End of picture text -->

Fig. 2: Illustration of DA<sup>2</sup> S which forces the softmax of architectural parameters _α_ and _β_ moving towards extreme points. Here, _a_<sup>_k_</sup> _i,j_<sup>denotestheweightonthe</sup> _k_ -th operation, and _bi,j_ denotes the weight between nodes _i_ and _j_ . Each color indicates a candidate, and the area of each region corresponds to the weight of corresponding candidate. This figure is best viewed in color. 

Summarizing the loss term on all edges obtains the operation loss: 


![](images/Davarmanesh_2020_Automated_Visual_Glitch_Detection_Deep_Learning.pdf-0007-05.png)


<!-- Start of picture text -->
L O ( α ) = � � L O i,j ( α ) . (3)<br>j i<j<br><!-- End of picture text -->

> exp _<u>{αi</u>_<sup>_o_</sup> _<u>,j</u>_<sup>_<u>}</u>_</sup> Note that Eq. (2) is an entropy-based loss function on <u>�</u> _o_<sup>_′_</sup> _∈O_<sup>exp</sup><sup>_{αo_</sup> _i,j_<sup>_<u>′</u>}_, the prob-</sup> 

ability of choosing _o_ ( _·_ ) as the operation of each ( _i, j_ ). Minimizing _L_<sup>O</sup> ( **_α_** ) pushes the weights of all operations to a one-hot distribution, _i.e._ , the probability of one operation is close to 1 _._ 0 while that of others are close to 0 _._ 0. Note that _L_<sup>_O_</sup> ( **_α_** ) is jointly optimized with _L_<sup>_C_</sup> ( **_α_** _,_ **_θ_** ), implying that when the search process is complete, the network parameters, **_θ_** , have been adjusted according to the one-hot **_α_** , consequently, the inaccuracy introduced by discretization is much smaller. 

Things become a bit different when we try to discrete **_β_** , because the configuration often requires to preserve more than one candidates, _e.g._ , according to the standard DARTS formulation, each node receives input from two previous nodes. To handle it, we add an extra term to the previous entropy loss and constrain the maximum value of any _βi,j_ to 1, and the overall loss is shown as: 


![](images/Davarmanesh_2020_Automated_Visual_Glitch_Detection_Deep_Learning.pdf-0007-09.png)


<!-- Start of picture text -->
2<br>exp {βi,j} exp {βi,j}<br>L E j ( β ) =  − � � βi,j − 2 , (4)<br>i<j � i ′ <j exp  {βi′,j} ·  log � i ′ <j exp  {βi′,j} + ����� B �����<br><!-- End of picture text -->

where _B_ = _{βi,j|i < j, βi,j >_ 0 _}_ . Note that the sum of 2 can be changed according to the search configuration. In the experimental part, we will show how this formulation generalizes to other types of desired topology, _e.g._ , preserving 4 or 6 out of 14 edges. 

8 Yunjie Tian, Chang Liu, Lingxi Xie, Jianbin Jiao, Qixiang Ye 

Similarly, summarizing this term on all nodes obtains the edge loss: 


![](images/Davarmanesh_2020_Automated_Visual_Glitch_Detection_Deep_Learning.pdf-0008-02.png)


<!-- Start of picture text -->
L E ( β ) = � L E j ( β ) , (5)<br>j<br><!-- End of picture text -->

and the discretization-aware objective function for architecture search is: 


![](images/Davarmanesh_2020_Automated_Visual_Glitch_Detection_Deep_Learning.pdf-0008-04.png)


<!-- Start of picture text -->
L ( θ ,  α ,  β ) =  L C ( α ,  θ ) +  L O ( α ) +  L E ( β ) , (6)<br><!-- End of picture text -->

### _•_ **Discretization Priority** 

Edge discretization and operation discretization depend on the performance estimation by each other. This warped paradox perplexes the community a lot for a long time, and can be eased by independently enforcing additional regularization on _α_ and _β_ . While, exploring the discretization priority of operation discretization and edge discretization further narrows the discretization gap. By introducing regularization control functions, the discretization-aware objective function for architecture search can be improved as: 


![](images/Davarmanesh_2020_Automated_Visual_Glitch_Detection_Deep_Learning.pdf-0008-07.png)


<!-- Start of picture text -->
L ( θ ,  α ,  β ) =  L C ( α ,  θ ) +  λc ( λ α L O ( α ) +  λ β L E ( β )) , (7)<br><!-- End of picture text -->

where _λc_ , _λ_ **_α_** and _λ_ **_β_** are regularization control factors related to classification accuracy, operation discretization and edge discretization, respectively. 

Considering the dynamic change of node connections, operation weights, and network parameters during the searching process, the regularization factors are defined as functions of training epochs, and simplified to be chosen from five representative increasing functions, as shown in Figure 5, to reveal the regular pattern of optimization priority. At early training epochs, the network is not well trained. The regularization factors are small so that the training focuses on network parameters. As the optimization process continues, the network gets better trained and more attentions are paid on selecting operations and edges. 

### **3.4 Relationship to Prior Work** 

There exist prior works to push the architectural parameters towards either 0 or 1 so as to align with the requirement of discretization. 

For example, FairDARTS [27] introduced the zero-one loss as _− K_<sup><u>1</u></sup> � _Kk_ =1<sup>_|σ_(</sup><sup>_αk_)</sup><sup>_−_0</sup><sup>_._5</sup><sup>_|_2</sup> to quantize the architectural parameters, _α_ , by using individual sigmoid rather than softmax, where _σ_ ( _·_ ) indicates the sigmoid function. In addition, by considering NAS as an annealing process in which the system converges to a less chaotic status, XNAS [28] proposed to reduce the temperature term of the crossentropy loss so that weaker candidates get eliminated. However, FairDARTS was not able to control the exact number of preserved candidates – sometimes there can be multiple weights pushing towards 1 but only one of them is allowed to be kept; on the other hand, XNAS cannot support more than one candidates to be preserved, which suffers limited flexibility when applied to multi-choice scenarios. In comparison, our approach can adjust the loss function according to the desired topology – we will show a variety of examples in Table 4. If needed, it can freely generalize to choose multiple operations for each edge. 

Discretization-Aware Architecture Search 9 

## **4 Experiments** 

In this section, we first describe the experimental settings. We then validate the effect of our discretization-aware search approach. We also report the performance of our approach on balanced and imbalanced configurations, and compare it with the state-of-the-arts. 

### **4.1 Experimental Settings** 

**Dataset** The commonly used CIFAR10 and ImageNet datasets are used to evaluate our network architecture search approach. CIFAR10 consists of 60K images, which are of a low spatial resolution of 32 _×_ 32. The images are equally distributed over 10 classes, with 50K training and 10K testing images. ImageNet contains 1,000 object categories, which consists of 1.3M high-resolution training images and 50K validation images. The images are almost equally distributed overall classes. Following the commonly used settings, we apply the mobile setting where the input image size is xed to be 224 _×_ 224 and the number of multi-add operations does not exceed 600M in the testing stage [10]. 

**Implementation Details.** Following DARTS as well as conventional architecture search approaches, we use an individual stage for architecture search, and after the optimal architecture is obtained, we use an additional process to train the classification model from scratch. During the search stage, the goal is to find the optimal _α_ and _β_ under the entropy-based discretization regularization in an end-to-end manner. We search architectures on CIFAR10 and then transfer to ImageNet. 

During the search procedure, we split the training data into two parts, one for each stage of the search process. As for search space, we follow DARTS but without zero as it requires to choose a low weight operation when zero has a advantage to form a standard cell. There are in total 7 options including 3 _×_ 3 and 5 _×_ 5 separable convolution, 3 _×_ 3 and 5 _×_ 5 dilated separable convolution, 3 _×_ 3 max-pooling, 3 _×_ 3 average-pooling, and skip-connect. 

When searching, the over-parameterized super-network is constructed by stacking 8 cells (6 normal cells and 2 reduction cells) with the initial number of channels 16, and each cell consists of N = 6 nodes. The 50K training set of CIFAR10 is split into two subsets with equal size, with one subset used for training network weights and the other used for architecture hyper-parameters. 

We train the super-network for 50 epochs and super-network weights are optimized by the momentum SGD algorithm, a momentum of 0 _._ 9, and a weight decay of 3 _×_ 10<sup>_−_4</sup> . The learning rate is reduced progressively to zero following a cosine schedule from an intial learning rate of 0 _._ 25 without restart. We use an Adam optimizer [29] for both _α_ and _β_ , both with a xed learning rate of 3 _×_ 10<sup>_−_4</sup> , a momentum of (0 _._ 5 _,_ 0 _._ 999) and a weight decay of 10<sup>_−_3</sup> [10]. The memory cost of our implementation is smaller than 11GB so that it can be trained on most modern GPUs. 

10 Yunjie Tian, Chang Liu, Lingxi Xie, Jianbin Jiao, Qixiang Ye 

Table 1: Comparison of classification error (%) with state-of-the-arts on CIFAR10. For DA<sup>2</sup> S, 2 _._ 42% and 2 _._ 51% are the best and average errors, respectively, and the search cost, 0 _._ 3 GPU-days, is reported on a single NVIDIA GTX-1080Ti GPU – on a Tesla-V100 GPU, the time is expected to be 0 _._ 2 GPU-days. 

|**Architecture**|**Test Err.**<br>**(%)**|**Params**<br>**(M)**|**Search Cost **<br>**(GPU-days)**|**Search Method**|
|---|---|---|---|---|
|DenseNet-BC [15]|3.46|25.6|-|manual|
|NASNet-A + cutout [2]|2.65|3.3|1800|RL|
|AmoebaNet-B + cutout [5]|2.55_±_0.05|2.8|3150|evolution|
|Hireachical Evolution [31]|3.75_±_0.12|15.7|300|evolution|
|PNAS [19]|3.41_±_0.09|3.2|225|SMBO|
|ENAS + cutout [7]|2.89|4.6|0.5|RL|
|NAONet-WS [25]|3.53|3.1|0.4|NAO|
|DARTS (1st order) + cutout [8]|3.00_±_0.14|3.3|0.4|gradient-based|
|DARTS (2nd order) + cutout [8]|2.76_±_0.09|3.3|1|gradient-based|
|SNAS (moderate) + cutout [32]|2.85_±_0.02|2.8|1.5|gradient-based|
|ProxylessNAS + cutout [33]|2.08|-|4.0|gradient-based|
|P-DARTS + cutout [9]|2.50|3.4|0.3|gradient-based|
|PC-DARTS + cutout [10]|2.57_±_0.07|3.6|**0.1**|gradient-based|
|BayesNAS + cutout [30]|2.81_±_0.04|3.4|0.2|gradient-based|
|DA<sup>2</sup>S (ours) + cutout|**2.42/2.51**_±_**0.09**|3.4|0.3|gradient-based|



### **4.2 Results on CIFAR10** 

In Table 1, we compare the proposed approach with the state-of-the-art approaches. It can be seen that our approach outperforms the baseline DARTS method with a large margin (2.42% vs. 2.76%), and outperforms recent gradientbased methods including P-DARTS [9], PC-DARTS [10], and BayesNAS [30]. Note that the significant performance gains are achieved with moderate parameter size (3.4 M) and computational cost (0.3 GPU days). The performance gains validate the effectiveness of our entropy-based regularization method and the importance of discretization-aware search itself. This part we will first introduce our approach to search standard cells (select 8 edges from 14 _i.e._ balanced configuration), and then to further illustrate the effectiveness of our approach, we will search non-standard cells (imbalanced configuration). 

**Operation and Edge Discretization** . There are 7 operations in total for all cells (the ‘none’ operation is not used). Each cell has 14 edges and the network consists of two kinds of cells: the normal cells and the reduction cells, that the network architecture depends on the search of 28 edges. That is to say _L_<sup>_O_</sup> ( _α_ ) is the sum of 28 operation entropy losses. And _L_<sup>_E_</sup> ( _β_ ) is the sum of all edge entropy losses, Eq. (4). In Eq. (7), we experimentally define that _λα_ = _λ_ 1, and _λβ_ = 4 _λ_ 2. Then we evaluate the results with _λ_ 1 and _λ_ 2 under different setting of functions shown in the Figure 5. 

In Figure 3, we present the evolution of softmax of operation weights _α_ on CIFAR10 with 14 edges in a normal cell. It can be seen that after about 20 training epochs, the softmax of operation weights begin to significantly differen- 

Discretization-Aware Architecture Search 

11 


![](images/Davarmanesh_2020_Automated_Visual_Glitch_Detection_Deep_Learning.pdf-0011-02.png)


<!-- Start of picture text -->
1.0 1.0 1.0 1.0 1.0 1.0 1.0<br>0.5 0.5 0.5 0.5 0.5 0.5 0.5<br>0.0 0.0 0.0 0.0 0.0 0.0 0.0<br>0 50 0 50 0 50 0 50 0 50 0 50 0 50<br>1.0 1.0 1.0 1.0 1.0 1.0 1.0<br>0.5 0.5 0.5 0.5 0.5 0.5 0.5<br>0.0 0.0 0.0 0.0 0.0 0.0 0.0<br>0 50 0 50 0 50 0 50 0 50 0 50 0 50<br>max pool avg pool skip connect sep conv 3�3 sep conv 5�5 dil conv 3�3 dil conv 5�5<br><!-- End of picture text -->

Fig. 3: Evolution of softmax of operation weights _α_ during the searching procedure in a normal cell on CIFAR10. The horizontal axis denotes training epoch and vertical axis softmax weight value. (Best viewed in color with zooming in). 


![](images/Davarmanesh_2020_Automated_Visual_Glitch_Detection_Deep_Learning.pdf-0011-04.png)


<!-- Start of picture text -->
0.5 0.5 0.5<br>0.4 0.4 0.4<br>0.3 0.3 0.3<br>0.2 0.2 0.2<br>0.1 0.1 0.1<br>0.0 0.0 0.0<br>0 20 40 0 20 40 0 20 40<br>node0 node1 node2 node3 node4<br><!-- End of picture text -->

Fig. 4: Evolution of softmax of edge weights _β_ of node3/4/5 during the searching procedure in a normal cell searched on CIFAR10. The horizontal axis denotes training epoch and vertical axis softmax weight value. 

tiate. At the final epoch, a single largest (towards 1) is obtained with the rest of small values (towards 0), which clearly demonstrate the effect of operation discretization. In Figure 4, we present the softmax evolution of _β_ , which validates the effect of edge discretization. Note that there are two edges selected at the same time for each pair of nodes, which shows the effectiveness of connection constraints in Eq. (4). 

**Discretization Priority.** The entropy loss function inevitably interferes the searching procedure of DARTS, particularly, at the early epochs. Therefore, we propose to progressively increase the regularization factors using monotonous functions as shown in Figure 5. In Table 2, we fix _λ_ 1 and _λ_ 2 as ‘const’ (equals 1 _._ 0), it can be seen that the fast increasing functions, such as ‘linear’ and ‘log’, outperform slow ones for regularization factor _λc_ , while ‘linear’ achives the best performance. It can be explained that moderately quick (linear) enhancement of the regularization on classification loss may have the smallest interference to the searching procedure. 

In Table 3, we test the priority of operation and edge discretization using different regularizaton control functions with _λc_ set to ‘linear’ as default. We fix _λ_ 1 as ‘const’ and evaluate _λ_ 2 using different control functions since the 8<sup>_th_</sup> epochs 

12 Yunjie Tian, Chang Liu, Lingxi Xie, Jianbin Jiao, Qixiang Ye 

Table 2: Classification errors (%) under different control functions for regularization factor _λc_ on CIFAR10. 

|baseline|**const**|**log**|**exp**|**step**|**linear**|
|---|---|---|---|---|---|
|2.76_±_0.09|2.64_±_0.14|2.56_±_0.06|2.78_±_0.11|2.60_±_0.07|**2.54**_±_**0.02**|



before which _λ_ 2 is fixed as 0. This means that the priority of operation discretization is higher than that of edge. Under this setting, the best performance (2.49%) is achieved by the ‘step’ function. On the other hand, we fix _λ_ 2 = 1 _._ 0 and change _λ_ 1 under the same conditions. The best performance (2.42%) is achieved by the ‘log’ function. 

The higher performance obtained by fixing _λ_ 2 = 1 _._ 0 shows that when the edge discretization dominates the search procedure, quick convergence of the topology of cell can lead the operation discretization-aware search converge better with fast increasing regularization control function (‘log’) utilized. 


![](images/Davarmanesh_2020_Automated_Visual_Glitch_Detection_Deep_Learning.pdf-0012-05.png)


<!-- Start of picture text -->
1.2<br>1.0<br>0.8<br>0.6<br>0.4 const<br>log<br>0.2 step<br>linear<br>0.0 exp<br>10 20 30 40 50<br>epoch<br>(. )<br><!-- End of picture text -->

|**Function**|_λ_1**=1.0**|_λ_|2**=1.0**|
|---|---|---|---|
||**best average **|**best **|**average**|
|const|2.71 2.74_±_0.03|2.53|2.56_±_0.03|
|linear|2.55 2.57_±_0.02|2.66|2.68_±_0.02|
|exp|2.51 2.53_±_0.02|2.57|2.60_±_0.03|
|step|**2.49** 2.54_±_0.05|2.51|2.57_±_0.06|
|log|2.61 2.64_±_0.03|**2.42**|2.51_±_0.09|



Fig. 5: Five regularization control functions. Table 3: Classification errors (%) when fixing either of _λ_ 1 This figure is best or _λ_ 2 while changing the other using the regularization viewed in color. control functions on CIFAR10. 

**Imbalanced Configurations.** In the above settings, it is defined that there are two inputs for each node in cells and the optimization objective is to select 8 out of 14 edges. This constraint largely reduces the difficulty of search, _i.e.,_ a random search can find architectures of moderate accuracy. To further validate the effectiveness and generalization of our approach, we search architectures with imbalanced configurations. Specifically, we break the setting about choosing 8 from 14 and choosing fewer edges to magnify the gap between architectures before and after discretization. 

Four configurations, namely, preserving 3–6 out of 14 edges, are used to validate our approach and compared it with DARTS. For DARTS, we use the default searched architecture and select 3, 4, 5, or 6 edges according to the weights of operations. For our approach, to select 3 edges, we pose edge entropyloss on node2 and node3, and select the largest one, and pose edge entropy-loss on node4 and node5 to select one on each. To select 4 edges, we pose edge entropy-loss on four inner nodes so that each of them has a single edge. For 5 

Discretization-Aware Architecture Search 13 

Table 4: Comparison (%) of re-training error and super-network accuracy between DARTS and DA<sup>2</sup> S under imbalanced configurations on CIFAR10. In the first column, 3 _<u>/</u>_ 14 indicates <u>preserving</u> 3 out of 14 edges. 

|**config**|**error**|**DARTS **<br>**para(M)**|**[8]**<br>**acc. drop**|**error**|**DA**<sup>**2**</sup>**S**<br>**para(M)**|**acc. drop**|
|---|---|---|---|---|---|---|
|3/14|5.83_±_1.21|1.5_±_0.2|87.87_→_10.03|**3.67**_±_**0.24**|1.9_±_0.2|85.52_→_64.23|
|4/14|4.79_±_1.17|1.9_±_0.3|87.87_→_09.87|**2.94**_±_**0.09**|2.5_±_0.1|85.63_→_85.42|
|5/14|3.23_±_0.08|2.2_±_0.2|87.87_→_10.12|**2.72**_±_**0.06**|2.9_±_0.1|84.76_→_71.85|
|6/14|2.91_±_0.05|2.7_±_0.1|87.87_→_09.96|**2.64**_±_**0.02**|3.0_±_0.1|84.29_→_64.24|




![](images/Davarmanesh_2020_Automated_Visual_Glitch_Detection_Deep_Learning.pdf-0013-03.png)


<!-- Start of picture text -->
skip_connectdil_conv_3x3sep_conv_3x32 max_pool_3x3 0<br>1 dil_conv_5x5 dil_conv_5x5<br>c_{k-2} sep_conv_3x3sep_conv_3x30 sep_conv_3x3 c_{k} c_{k-2} max_pool_3x3dil_conv_5x5 1 c_{k}<br>c_{k-1} skip_connect c_{k-1} dil_conv_3x3max_pool_3x3 2<br>sep_conv_3x3 3 skip_connect 3<br><!-- End of picture text -->

(a) the normal cell found on CIFAR10 

(b) the reduction cell found on CIFAR10 

Fig. 6: Normal cell and reduction cell searched on CIFAR10. 

edge edges, we select two on node5 and one on other 3 nodes. For 6 edges, we select two on node4/node5 and one on node2/node3. 

In Table 4, the performance under imbalanced configurations of DARTS and our approach is compared. Under imbalanced configurations, the performance of DARTS dramatically drops in a large margin around [77.75-78.00], which demonstrates that the discretization process does bring a significant gap before and after prunning. Such gap has unpredictable impact upon searched architecture. In contrast, with discretization-aware constraint, our approach achieves relatively stable performance that the classification accuracy drop are significantly reduced to [0.21, 21.29]. For each configuration, it outperforms DARTS with significant margins (2.16%, 1.75%, 0.51%, 0.27%) after re-training. 

### **4.3 Results on ImageNet** 

This part we use large-scale ImageNet to test the transferability of cells searched on CIFAR10 as shown in Figure 6. Same configuration as DARTS is adopt, _i.e._ , the entire network is construct by stacking 14 cells with an initial channel number of 48. We train the network for 250 epochs from scratch with batch size 1024 on 8 Tesla V100 GPUs. An SGD optimizer is used for optimizing the network parameters with an initial learning rate of 0 _._ 5 (decayed linearly after each epoch), and also a momentum of 0.9 and a weight decay of 3 _×_ 10<sup>_−_5</sup> . Other enhancements including label smoothing [34] and auxiliary loss are used during training, and learning rate warmup [35] is applied for the first 5 epochs. 

14 Yunjie Tian, Chang Liu, Lingxi Xie, Jianbin Jiao, Qixiang Ye 

Table 5: Comparison of classification error (%) on ImageNet under the mobile setting <u>(no</u> larger than 600M FLOPs). 

|**Architecture**|**Test E**|**rr. (%) **|**Params**|_×_+|**Search Cost **|**Search Method**|
|---|---|---|---|---|---|---|
||**top-1**|**top-5**|**(M)**|**(M) **|**(GPU-days)**||
|Inception-v1 [36]|30.2|10.1|6.6|1448|-|manual|
|MobileNet [37]|29.4|10.5|4.2|569|-|manual|
|ShuffleNet 2_×_ (v1) [38]|26.4|10.2|_∼_5|524|-|manual|
|ShuffleNet 2_×_ (v2) [39]|25.1|-|_∼_5|591|-|manual|
|NASNet-A [2]|26.0|8.4|5.3|564|1800|RL|
|AmoebaNet-C [5]|24.3|7.6|6.4|570|3150|evolution|
|PNAS [19]|25.8|8.1|5.1|588|225|SMBO|
|MnasNet-92 [24]|25.2|8.0|4.4|388|-|RL|
|DARTS (2nd order) [8]|26.7|8.7|4.7|574|4.0|gradient-based|
|SNAS (mild) [32]|27.3|9.2|4.3|522|1.5|gradient-based|
|ProxylessNAS (GPU) [33]|24.9|7.5|7.1|465|8.3|gradient-based|
|P-DARTS (CIFAR10) [9]|24.4|7.4|4.9|557|0.3|gradient-based|
|PC-DARTS (CIFAR10) [10]|25.1|7.8|5.3|586|0.1|gradient-based|
|BayesNAS [30]|26.5|8.9|3.9|-|0.2|gradient-based|
|DA<sup>2</sup>S (CIFAR10)|**24.4**|7.3|5.0|565|0.3|gradient-based|



In Table 5, we evaluate the proposed approach and compare the result with the state-of-the-art approaches under the mobile setting (the FLOPs does not exceed 600M). DA<sup>2</sup> S outperforms the direct baseline, DARTS, by a significant margin of 2 _._ 3% (an error rate of 24 _._ 4% vs. 26 _._ 7%). DA<sup>2</sup> S also produces competitive performance among some recently published work including P-DARTS, PC-DARTS, and BeyesNAS, when the network architecture is searched on CIFAR and transferred to ImageNet. This further verifies the superiority of our DA<sup>2</sup> S in mitigating the discretization gap in the differentiable architecture search framework. 

## **5 Conclusions** 

In this paper, we propose a discretization-aware NAS method, which works by introducing an entropy-based loss term to push the super-network towards a discretization-friendly status according to the pre-defined target. This strategy can be applied to either selecting an operator for each edge, or selecting a fixed number of edges for each node. Experiments on standard image classification benchmarks demonstrate the superiority of our approach, in particular, under some imbalanced configurations which were not studied before. 

This work provides another evidence that one-shot neural architecture search can benefit from shrinking the gap between the super-network and sub-networks. As the search space becomes more complicated in the future, we expect our approach to serve as a standard tool to alleviate the discretization gap. We also look forward to investigate some uncovered problems, _e.g._ , whether discretization can be done in a gradual manner so as to further reduce the error. 

Discretization-Aware Architecture Search 15 

## **References** 

1. Zoph, B., Le, Q.V.: Neural architecture search with reinforcement learning. In: ICLR. (2017) 

2. Zoph, B., Vasudevan, V., Shlens, J., Le, Q.V.: Learning transferable architectures for scalable image recognition. In: IEEE CVPR. (2018) 8697–8710 

3. Real, E., Moore, S., Selle, A., Saxena, S., Suematsu, title=Large-scale evolution of image classifiers, Y.L., Tan, J., Le, Q.V., Kurakin, A. In: ICML. (2017) 2902–2911 

4. Xie, L., Yuille, A.: Genetic cnn. In: IEEE ICCV. (2017) 1388–1397 

5. Real, E., Aggarwal, A., Huang, Y., Le, Q.V.: Regularized evolution for image classifier architecture search. In: AAAI. (2019) 4780–4789 

6. Brock, A., Lim, T., Ritchie, J.M., Weston, N.: SMASH: one-shot model architecture search through hypernetworks. In: ICLR. (2018) 

7. Pham, H., Guan, M.Y., Zoph, B., Le, Q.V., Dean, J.: Efficient neural architecture search via parameter sharing. In: ICML. (2018) 4092–4101 

8. Liu, H., Simonyan, K., Yang, Y.: DARTS: Differentiable architecture search. In: ICLR. (2019) 

9. Chen, X., Xie, L., Wu, J., Tian, Q.: Progressive differentiable architecture search: Bridging the depth gap between search and evaluation. In: IEEE ICCV. (2019) 

10. Xu, Y., Xie, L., Zhang, X., Chen, X., Qi, G.J., Tian, Q., Xiong, H.: PC-DARTS: partial channel connections for memory-efficient differentiable architecture search. arXiv preprint arXiv:1907.05737 

11. LeCun, Y., Bengio, Y., Hinton, G.E.: Deep learning. Nature **521** (7553) (2015) 436–444 

12. Alex, K., Ilya, S., E, H.G.: Imagenet classification with deep convolutional neural networks. In: NeurIPS. (2012) 1106–1114 

13. Simonyan, K., Zisserman, A.: Very deep convolutional networks for large-scale image recognition. In: ICLR. (2015) 

14. He, K., Zhang, X., Ren, S., Sun, J.: Deep residual learning for image recognition. In: IEEE CVPR. (2016) 770–778 

15. Huang, G., Liu, Z., Van Der Maaten, L., Weinberger, K.Q.: Densely connected convolutional networks. In: IEEE CVPR. (2017) 2261–2269 

16. : http://www.cs.ubc.ca/labs/beta/projects/autoweka 

17. Ghiasi, G., Lin, T., Le, Q.V.: NAS-FPN: learning scalable feature pyramid architecture for object detection. In: IEEE CVPR. (2019) 7036–7045 

18. Liu, C., Chen, L.C., Schroff, F., Adam, H., Hua, W., Yuille, A., Fei-Fei, L.: Autodeeplab: Hierarchical neural architecture search for semantic image segmentation. In: IEEE CVPR. (2019) 82–92 

19. Liu, C., Zoph, B., Neumann, M., Shlens, J., Hua, W., Li, L.J., Fei-Fei, L., Yuille, A., Huang, J., Murphy, K.: Progressive neural architecture search. In: ECCV. (2018) 540–555 

20. Cai, H., Chen, T., Zhang, W., Yu, Y., Wang, J.: Efficient architecture search by network transformation. In: AAAI. (2018) 2787–2794 

21. Stamoulis, D., Ding, R., Wang, D., Lymberopoulos, D., Priyantha, B., Liu, J., Marculescu, D.: Single-path nas: Designing hardware-efficient convnets in less than 4 hours. In: arXiv preprint arXiv:1904.02877. (2019) 

22. Chu, X., Zhang, B., Xu, R., Li, J.: Fairnas: Rethinking evaluation fairness of weight sharing neural architecture search. ArXiv **abs/1907.01845** (2019) 

23. Howard, G., Sandler, M., Chu, G., Chen, L.C., Chen, B., Tan, M., Wang, W., Zhu, Y., Pang, R., Vasudevan, V., Le, Q.V., Adam, H.: Searching for mobilenetv3. In: IEEE ICCV. (2019) 1314–1324 

16 Yunjie Tian, Chang Liu, Lingxi Xie, Jianbin Jiao, Qixiang Ye 

24. Tan, M., Chen, B., Pang, R., Vasudevan, V., Le, Q.V.: Mnasnet: Platform-aware neural architecture search for mobile. IEEE CVPR (2019) 2820–2828 

25. Luo, R., Tian, F., Qin, T., Chen, E., Liu, T.Y.: Neural architecture optimization. In: NeurIPS. (2018) 7827–7838 

26. Zela, A., Elsken, T., Saikia, T., Marrakchi, Y., Brox, T., Hutter, F.: Understanding and robustifying differentiable architecture search. (2019) 

27. Chu, X., Zhou, T., Zhang, B., Li, J.: Eliminating unfair advantages in differentiable architecture search. (2019) 

28. Nayman, N., Noy, A., Ridnik, T., Friedman, I., Jin, R., Zelnik, L.: Xnas: Neural architecture search with expert advice. In: NeurIPS. (2019) 

29. Kingma, D.P., Ba, J.: Adam: A method for stochastic optimization. In: ICLR. (2015) 

30. Zhou, H., Yang, M., Wang, J., Pan, W.: BayesNAS: A Bayesian approach for neural architecture search. In: ICML. (2019) 7603–7613 

31. Liu, H., Simonyan, K., Vinyals, O., Fernando, C., Kavukcuoglu, K.: Hierarchical representations for efficient architecture search. In: ICLR. (2018) 

32. Xie, S., Zheng, H., Liu, C., Lin, L.: SNAS: Stochastic neural architecture search. In: ICLR. (2019) 

33. Cai, H., Zhu, L., Han, S.: ProxylessNAS: Direct neural architecture search on target task and hardware. In: ICLR. (2019) 

34. Szegedy, C., Vanhoucke, V., Ioffe, S., Shlens, J., Wojna, Z.: Rethinking the inception architecture for computer vision. In: IEEE CVPR. (2016) 2818–2826 

35. Goyal, P., Doll´ar, P., Girshick, R., Noordhuis, P., Wesolowski, L., Kyrola, A., Tulloch, A., Jia, Y., He, K.: Accurate, large minibatch SGD: Training ImageNet in 1 hour. arXiv preprint arXiv:1706.02677 (2017) 

36. Szegedy, C., Liu, W., Jia, Y., Sermanet, P., Reed, S., Anguelov, D., Erhan, D., Vanhoucke, V., Rabinovich, A.: Going deeper with convolutions. In: IEEE CVPR. (2015) 1–9 

37. Howard, A.G., Zhu, M., Chen, B., Kalenichenko, D., Wang, W., Weyand, T., Andreetto, M., Adam, H.: MobileNets: Efficient convolutional neural networks for mobile vision applications. arXiv preprint arXiv:1704.04861 (2017) 

38. Zhang, X., Zhou, X., Lin, M., Sun, J.: Shufflenet: An extremely efficient convolutional neural network for mobile devices. In: IEEE CVPR. (2018) 6848–6856 

39. Ma, N., Zhang, X., Zheng, H.T., Sun, J.: Shufflenet v2: Practical guidelines for efficient cnn architecture design. In: ECCV. (2018) 122–138 

