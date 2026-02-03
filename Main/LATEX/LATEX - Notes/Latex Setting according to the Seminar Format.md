Step 1: Create a new Overleaf project
New Project → Blank Project → name it `Seminar_Format`

Step 2: Set page layout, font, size
Your requirements:

* Font: Times New Roman
* Font size: 11 pt
* Margins: 1 inch
* Single column

Use this preamble:

```latex
\documentclass[11pt]{article}

% Page layout
\usepackage[a4paper,margin=1in]{geometry}

% Times New Roman font
\usepackage{newtxtext,newtxmath}

% For bold headings and formatting
\usepackage{titlesec}

% For figures and tables
\usepackage{graphicx}
\usepackage{caption}

% Numbering of sections and subsections
\setcounter{secnumdepth}{2}

% Section format
\titleformat{\section}
{\bfseries\fontsize{14}{16}\selectfont}
{\thesection.}{1em}{}

\titleformat{\subsection}
{\bfseries\fontsize{12}{14}\selectfont}
{\thesubsection.}{1em}{}
```

---

Step 3: Seminar Heading block

Rules:

* All capitals
* Bold
* 16 pt
* Centered

```latex
\begin{document}

\begin{center}
{\bfseries\fontsize{16}{18}\selectfont SEMINAR HEADING}\\[1em]

Name of the Student\\
Central Department of Computer Science and Information Technology\\
Institute of Science and Technology\\
Tribhuvan University\\
February 20, 2009
\end{center}
```

(Notice: you did not write the word *Date*, only the actual date.)

---

Step 4: Normal text
Times New Roman, 11 pt is already set:

```latex
This is normal seminar text written here. Definitions, scientists' names etc.
can be written in \textit{italic} when needed.
```

---

Step 5: Sections and subsections

Rules:

* Section: Bold, 14 pt, First letters capital
* Subsection: Bold, 12 pt, First letters capital
* Numbered and left aligned

```latex
\section{Introduction}

This is the introduction section.

\subsection{Response Time Variability}

This is a subsection under introduction.
```

It will automatically show as:

```
1. Introduction  
1.1 Response Time Variability
```

---

Step 6: Figures

Rules:

* Numbering: Figure 1, Figure 2 …
* Caption compulsory

```latex
\begin{figure}[h]
\centering
\includegraphics[width=0.6\textwidth]{example-image}
\caption{System Architecture}
\end{figure}
```

---

Step 7: Tables

Rules:

* Numbering: Table 1, Table 2 …
* Caption compulsory

```latex
\begin{table}[h]
\centering
\caption{Performance Comparison}
\begin{tabular}{|c|c|c|}
\hline
Algorithm & Time & Accuracy \\
\hline
A & 10 ms & 90\% \\
B & 12 ms & 92\% \\
\hline
\end{tabular}
\end{table}
```

---

Step 8: Citation style inside text

Your format:

```
Miltenburg and Goldstein [34] extend...
```

In LaTeX you simply write:

```latex
Miltenburg and Goldstein [34] extend the formulation to multi-level system.
The problem of optimal scheduling is considered in [13].
```

(No BibTeX needed if your department wants manual formatting.)

---

Step 9: References section

Rules:

* One single list
* Alphabetic order by last name
* No separation like “Books”, “Journals”

```latex
\section{References}

[1] N. Brauner and Y. Crama, \textit{The Maximum Deviation Just-In-Time Scheduling Problem},
Discrete Applied Mathematics, 134 (2004), 25–50.

[2] K. H. Rosen, \textit{Discrete Mathematics and its Applications}
(TATA McGraw Hill Edition, 2003, New Delhi).

[3] Y. Stoskov, V. S. Tanaev and F. Werner, \textit{Stability Radius of an Optimal Schedule:
A Survey and Recent Developments}, in Industrial Application of Combinatorial Optimization
(Kluwer Academic Publishers, 1998), 72–108.

[4] T. N. Dhamala, \textit{Shop Scheduling Solution-Spaces with Algebraic Characterizations}
(Ph.D. Thesis, Otto-von-Guericke University, Magdeburg, Germany, 2002).
```

---

Step 10: Complete skeleton you can paste in Overleaf

```latex
\documentclass[11pt]{article}
\usepackage[a4paper,margin=1in]{geometry}
\usepackage{newtxtext,newtxmath}
\usepackage{titlesec}
\usepackage{graphicx}
\usepackage{caption}

\titleformat{\section}
{\bfseries\fontsize{14}{16}\selectfont}
{\thesection.}{1em}{}

\titleformat{\subsection}
{\bfseries\fontsize{12}{14}\selectfont}
{\thesubsection.}{1em}{}

\begin{document}

\begin{center}
{\bfseries\fontsize{16}{18}\selectfont SEMINAR HEADING}\\[1em]
Name of the Student\\
Central Department of Computer Science and Information Technology\\
Institute of Science and Technology\\
Tribhuvan University\\
February 20, 2009
\end{center}

\section{Introduction}
This is the introduction of the seminar.

\subsection{Response Time Variability}
This subsection explains response time variability.

Miltenburg and Goldstein [34] extend the formulation to multi-level systems.
The problem of optimal scheduling is considered in [13].

\section{References}

[1] N. Brauner and Y. Crama, \textit{The Maximum Deviation Just-In-Time Scheduling Problem},
Discrete Applied Mathematics, 134 (2004), 25–50.

[2] K. H. Rosen, \textit{Discrete Mathematics and its Applications}
(TATA McGraw Hill Edition, 2003, New Delhi).

[3] Y. Stoskov, V. S. Tanaev and F. Werner, \textit{Stability Radius of an Optimal Schedule:
A Survey and Recent Developments}, in Industrial Application of Combinatorial Optimization
(Kluwer Academic Publishers, 1998), 72–108.

[4] T. N. Dhamala, \textit{Shop Scheduling Solution-Spaces with Algebraic Characterizations}
(Ph.D. Thesis, Otto-von-Guericke University, Magdeburg, Germany, 2002).

\end{document}
```

---


