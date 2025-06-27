#### Sample Example
```md
\documentclass{article}
\begin{document}
First document. This is a simple example, with no 
extra parameters or packages included.
\end{document}
```

---
#### Sample for Seminar I Report
```md
\documentclass[12pt]{article}
\usepackage[top=1in, bottom=1in, left=1in, right=1in]{geometry} % 1-inch margins
\usepackage{times} % Times New Roman font
\usepackage{setspace} % For line spacing
\onehalfspacing % 1.5 line spacing
\usepackage{graphicx} % For including images
\usepackage[natbibapa]{apacite} % For APA style citations

\title{Seminar Title}
\author{Your Name}
\date{\today}

\begin{document}

% Cover Page & Title Page
\begin{titlepage}
    \centering
    \vspace*{2cm}
    {\LARGE Seminar I Report\par}
    \vspace{1cm}
    {\Huge \textbf{Your Seminar Title}\par}
    \vspace{2cm}
    {\Large Submitted by:\par}
    {\Large Your Name\par}
    \vspace{1cm}
    {\Large Submitted to:\par}
    {\Large Department of Computer Science\par}
    \vspace{2cm}
    {\Large Tribhuvan University\par}
    {\large Institute of Science and Technology\par}
    \vfill
    {\large \today\par}
\end{titlepage}

% Abstract
\begin{abstract}
    This is where you write a brief summary of your seminar topic, typically 150-250 words. 
    The abstract should clearly state the purpose of your seminar, the main points you will cover, 
    and any significant conclusions you have drawn from your research. It should be concise yet 
    informative enough to give readers a clear understanding of your seminar's content.
\end{abstract}

\newpage

% Table of Contents
\tableofcontents
\newpage

% Chapter 1: Introduction
\section{Introduction}
\label{sec:introduction}
This section introduces your seminar topic. You should:
\begin{itemize}
    \item Provide background information on your topic
    \item Explain why this topic is important or relevant
    \item State the objectives of your seminar
    \item Give an overview of what you will cover
\end{itemize}

% Chapter 2: Previous Works, Discussions and Findings
\section{Previous Works, Discussions and Findings}
\label{sec:previous}
This is the main body of your seminar report. Here you should:
\begin{itemize}
    \item Review existing literature and research on your topic
    \item Compare different approaches or solutions
    \item Present key findings from your research
    \item Analyze and discuss these findings
\end{itemize}

For example, you might cite a reference like \cite{Bishop2009} when discussing computer security concepts.

% Chapter 3: Conclusion
\section{Conclusion}
\label{sec:conclusion}
Summarize the key points of your seminar. You should:
\begin{itemize}
    \item Restate your main findings
    \item Discuss the implications of your research
    \item Suggest areas for future work
    \item Provide a final thought on the topic
\end{itemize}

% References
\bibliographystyle{apacite}
\bibliography{references} % Create a references.bib file for your citations

\end{document}
```
###### Output
![](../../../Images/First_Sem_Images/Simplest_working_example_LaTeX_document.pdf)


## Reference
[Latex-YouTube](https://www.youtube.com/watch?v=lgiCpA4zzGU&list=PLKc3Lw_EvMR7yfm6PunZ98x-OOv5nZnox)
[Overleaf](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes#What_is_LaTeX?)