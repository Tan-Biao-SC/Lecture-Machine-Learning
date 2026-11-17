# windows系统中python编程环境配置指南

Date: 2026-11-13

Version: 1.0

## 1. 概述

> [!IMPORTANT]
>
> *我们要用到哪些软件？各自有什么作用？*

本指南介绍如何在`windows`系统（适用于`win10`和`win11`）中配置并管理`python`编程环境。在数据科学中，我们通常使用`Anaconda`软件作为`python`编程环境的管理软件。为了方便大家以后持续学习和使用`python`编程语言、数据分析、机器学习以及人工智能算法等，本课程建议使用如下软件：

- `Anaconda`：其主要作用是管理python编程环境，我们可以为不同的任务创建不同的*虚拟环境*，这样可以确保任务之间不相互干扰；同时它也提供了很多实用工具，如集成开发环境`spyder`、数据分析与可视化常用的`Jupyter Notebook`等。
- `vscode`：这是由微软开发的开源文本编辑器，它的作用是帮助我们更好的写代码。比如你写报告要用的`word`，写代码我们就要用文本编辑器。其实你们电脑中的“记事本”软件就是一个文本编辑器，但是`vscode`的功能更强大，使用也更方便。
- `Jupyter Notebook`: 它是数据分析中最常用的工具，可以在一个文件中记录文字、图片，同时也可以运行代码并查看其结果。在数据分析和挖掘中可以直观地展示我们的探索过程和结果。这个工具无需单独安装，它包含在`Anaconda`中。

注意，`Anaconda`因为包含了很多实用工具，所以其占用硬盘空间较大。对于一些高阶用户，他们清楚自己需要哪些工具，所以通常会使用`Miniconda`；`Miniconda`提供了和`Anaconda`一样的`python`编程环境管理功能，但是删除了很多实用工具，用户需要自己下载安装。

> [!NOTE]
>
> **本课程建议先使用`Anaconda`**，等大家熟悉编程后再根据自己的需求选择。

## 2. Anaconda安装与基本使用

### 2.1 下载`Anaconda`

Anaconda是一个免费软件，可以在其官网：https://www.anaconda.com/download 下载。

1. 进入官网下载页面后，单击`Skip to download`，会跳转到下载页面

![image-20261113172803362](https://cdn.jsdelivr.net/gh/Tan-Biao-SC/imgurl/markdown/image-20261113172803362.png)

2. 在下载页面中：windows -> Anaconda Distribution -> 单击Windows 64-bit (x86_64) graphical installer ，即可开始下载。

![image-20261113172931535](https://cdn.jsdelivr.net/gh/Tan-Biao-SC/imgurl/markdown/image-20261113172931535.png)

### 2.2 安装`Anaconda`

双击上一步中下载好的安装包，进入安装向导中，后续安装步骤见下图：

1. 进入安装提示界面，单击`next`

![image-20261113173729430](https://cdn.jsdelivr.net/gh/Tan-Biao-SC/imgurl/markdown/image-20261113173729430.png)

2. 同意使用协议，单击`I Agree`

![image-20261113174056687](https://cdn.jsdelivr.net/gh/Tan-Biao-SC/imgurl/markdown/image-20261113174056687.png)

3. 选择安装类型，建议选择`Just Me`，意思是只为当前windows用户安装；`All Users`配置复杂，且极易出现问题，**不要选！不要选！不要选！**

![image-20261113174147721](https://cdn.jsdelivr.net/gh/Tan-Biao-SC/imgurl/markdown/image-20261113174147721.png)

4. 设置安装路径，默认安装位置是`C:\Users\用户名\anaconda3`；建议安装到其他硬盘分区（请记住自己安装到什么位置的）；**注意：安装路径一定不要有中文**

![image-20261113174324623](https://cdn.jsdelivr.net/gh/Tan-Biao-SC/imgurl/markdown/image-20261113174324623.png)

5. 高级安装选项设置；这里建议全选，每项的大致含义如下：
   1. 第1项：创建快捷方式
   2. 第2项：自动添加系统环境，这样可以让系统软件识别到`Anaconda`创建的编程环境
   3. 第3项：设置`Anaconda`中默认的`python`版本为3.14
   4. 第4项：清除安装过程中产生的缓存文件

![image-20261113174429105](https://cdn.jsdelivr.net/gh/Tan-Biao-SC/imgurl/markdown/image-20261113174429105.png)

6. 等待安装完成，通常需要几分钟

![image-20261113220843721](https://cdn.jsdelivr.net/gh/Tan-Biao-SC/imgurl/markdown/image-20261113220843721.png)

7. 安装完成提示；这两项可选，两项的含义如下：
   1. 第1项：打开`Anaconda Navigator`软件，见后面的图
   2. 第2项：在浏览器中打开`Anaconda`主页

![image-20261113220908496](https://cdn.jsdelivr.net/gh/Tan-Biao-SC/imgurl/markdown/image-20261113220908496.png)

![image-20261113220930720](https://cdn.jsdelivr.net/gh/Tan-Biao-SC/imgurl/markdown/image-20261113220930720.png)

![image-20261113221210492](https://cdn.jsdelivr.net/gh/Tan-Biao-SC/imgurl/markdown/image-20261113221210492.png)

**恭喜！Anaconda安装顺利完成~**

### 2.3 初步认识`Anaconda`（可以跳过）

`Anaconda`软件安装完成后，系统中会增加以下五个软件：

- `Anaconda Navigator`：`Anaconda`软件的导航界面
- `Anaconda powershell promt`：基于`powershell`的命令行工具
- `Anaconda promt`：基于`cmd`的命令行工具
- `Jupyter Notebook`：笔记本
- `Spyder`：集成开发环境（我们用不到，不过以后大家可以深入学习`python`编程时可以尝试）

![image-20261113222420465](https://cdn.jsdelivr.net/gh/Tan-Biao-SC/imgurl/markdown/image-20261113222420465.png)

#### 2.3.1 `Anaconda Navigator`

`Anaconda Navigator`是`Anaconda`软件的导航界面，在这里我们可以看到已经创建的虚拟环境和其中安装的工具。

![image-20261113222901266](https://cdn.jsdelivr.net/gh/Tan-Biao-SC/imgurl/markdown/image-20261113222901266.png)

> [!TIP]
>
> 一般我们很少使用这个界面，后面会介绍使用`conda`命令管理编程环境；但是一开始不熟悉时，可以借助这个界面帮助我们查看这些环境。

#### 2.3.2 `Anaconda powershell promt`和`Anaconda promt`

这两个软件几乎一样，区别只在于`Anaconda powershell promt`可以运行全部`windows`命令，因此我们一般用它。进入软件，会看到一个黑框框，在其中输入

```powershell
python
```

点击`enter`键就可以进入python解释器，并可以在其中运行`python`代码。

![image-20261113231145613](https://cdn.jsdelivr.net/gh/Tan-Biao-SC/imgurl/markdown/image-20261113231145613.png)

> [!tip]
>
> 可以输入`exit`退出python解释器；也可以使用快捷键`ctrl + d`退出。

也可以通过它打开`Jupyter Notebook`工具，执行

```powershell
jupyter notebook
```

就可以在浏览器中打开`Jupyter Notebook`软件。

![image-20261113231643104](https://cdn.jsdelivr.net/gh/Tan-Biao-SC/imgurl/markdown/image-20261113231643104.png)

> [!tip]
>
> 直接点击`Jupyter Notebook`打开的也是这个页面。

### 2.4 在`powershell`中使用`Anaconda`

我们也可以在`windows`系统提供的`powershell`工具中通过`conda` 命令来调用`Anaconda`软件。输入`conda`命令并运行后看到如下图片即证明`Anaconda`的安装和配置正确。

![image-20261115170847870](https://cdn.jsdelivr.net/gh/Tan-Biao-SC/imgurl/markdown/image-20261115170847870.png)

> [!caution]
>
> 如果在安装过程的第5步中没有选择第2项，那么`windows`系统将无法识别到已经安装好的`Anaconda`软件，在`powershell`中运行`conda`命令会提示未找到该命令。此时，需要将`Anaconda`的运行路径添加到*系统环境变量*中。

**具体操作如下：**

1. **通过系统设置打开**：【设置】->【系统】->【系统信息】-> 点击【高级系统设置

![image-20261115172716809](https://cdn.jsdelivr.net/gh/Tan-Biao-SC/imgurl/markdown/image-20261115172716809.png)

![image-20261115172736738](https://cdn.jsdelivr.net/gh/Tan-Biao-SC/imgurl/markdown/image-20261115172736738.png)

2. 进入系统属性，在“高级”选项卡中点击“环境变量”

![image-20261115172851986](https://cdn.jsdelivr.net/gh/Tan-Biao-SC/imgurl/markdown/image-20261115172851986.png)

3. 在“系统变量” Path中添加如下目录：
   - anaconda安装的目录 
   -  anaconda/scripts的目录 
   - bin的目录 

![image-20261115174059347](https://cdn.jsdelivr.net/gh/Tan-Biao-SC/imgurl/markdown/image-20261115174059347.png)

![image-20261115174251345](https://cdn.jsdelivr.net/gh/Tan-Biao-SC/imgurl/markdown/image-20261115174251345.png)

![image-20261115174801843](https://cdn.jsdelivr.net/gh/Tan-Biao-SC/imgurl/markdown/image-20261115174801843.png)

### 2.5 `Anacodna`的基本用法

>[!TIp]
>
>虚拟环境就是**“专项目专用”的独立小房间**——在房间里怎么折腾、装什么版本，都不会影响隔壁房间的其他项目。

通常我们采用命令行工具`conda`进行`python`编程环境的管理，所谓管理通俗来说就是进行增、删、查、改等操作。对于本课程，我们需要掌握如何创建环境、激活环境以及退出当前环境。

1. 查看当前系统中的虚拟环境，在powershell中运行如下命令

```powershell
conda env list
# conda 主程序名称，告诉系统你要调用 Conda 工具
# env 子命令模块（Environment 的缩写），表示接下来的操作都是针对“虚拟环境”本身的（比如创建、删除、查看环境，而不是安装某个具体的 Python 包）
# list 具体操作，列出所有环境
```

运行结果见下图

![image-20261115203248503](https://cdn.jsdelivr.net/gh/Tan-Biao-SC/imgurl/markdown/image-20261115203248503.png)

2. 创建新环境，在powershell中运行如下命令

```powershell
conda create -n ml-course python=3.12
# conda 指调用conda工具
# create 核心动作（创建），指示 Conda 新建一个独立的“小工具箱”
# • -n ml-course：指定新环境的名字。
#	• -n 是 --name（名称）的缩写。
#	• ml-course 是你给这个环境起的名字（你可以根据项目随意命名，比如 web-dev、test1，建议用英文、数字和短横线，避免使用中文或空格）。
# python=3.12：指定该环境中安装的 Python 版本。它会专门为这个新环境下载一套独立的 Python 3.12 以及 pip 等最基础的配套工具，完全不会影响你电脑里 base 环境原本的 Python 版本。
```

此时系统的虚拟环境如下：

![image-20261115203720703](https://cdn.jsdelivr.net/gh/Tan-Biao-SC/imgurl/markdown/image-20261115203720703.png)

3. 激活指定环境

```powershell
conda activate ml-course
# 激活名为 ml-course 的虚拟环境
```

![image-20261115203950824](https://cdn.jsdelivr.net/gh/Tan-Biao-SC/imgurl/markdown/image-20261115203950824.png)

4. 退出当前环境

```powershell
conda deactivate
# 这条命令可以退出当前环境，并回退到进入该环境之前的环境中
```

![image-20261115204201913](https://cdn.jsdelivr.net/gh/Tan-Biao-SC/imgurl/markdown/image-20261115204201913.png)

`conda`的功能很强大，我们暂时只需要掌握上述应用即可；更多的功能及用法可以查阅官方文档：https://www.anaconda.com/docs/getting-started/working-with-conda/main。

## 3. vscode安装与配置

### 3.1 vscode的安装与基本使用

vscode官方下载网站：https://code.visualstudio.com/

其安装过程较为简单，详细安装步骤和基本使用方法可以参考这篇文章：https://zhuanlan.zhihu.com/p/698865320 （**建议看一下使用方法**）

### 3.2 vscode配置

安装好vscode后还需要安装如下扩展，才能正确识别conda中创建的虚拟环境：

-  Python — Microsoft （**必装**）

  提供 Python 代码运行、调试、解释器选择以及基本的环境管理功能

- Python Environments — Microsoft （推荐）

  提供更集中的 Python 环境发现、创建、切换与管理功能，包括 Conda 环境
  
- Jupyter — Microsoft （**必装**）

  支持在 VS Code 中运行 `.ipynb` 文件、选择 Notebook 内核、执行代码单元

其中，Python 是基础扩展；Python Environments 是环境管理增强工具；Jupyter 则适合你的课程后续开展 Notebook 教学。

![image-20261115210953054](https://cdn.jsdelivr.net/gh/Tan-Biao-SC/imgurl/markdown/image-20261115210953054.png)



---

恭喜！完成上述安装和配置后，你就拥有完整python编程环境了。

