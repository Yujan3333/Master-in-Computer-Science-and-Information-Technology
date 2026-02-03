## Overleaf

Step 1: Open Overleaf
Go to: [https://www.overleaf.com](https://www.overleaf.com)
Create an account (Google login is easiest).

Step 2: Create a new project
After login:

* Click **“New Project”**
* Choose **“Blank Project”**
* Give it a name (e.g., `MyFirstLatexDoc`)

You will see:

* Left: file list
* Middle: LaTeX editor
* Right: PDF preview (auto-compiles)

Step 3: Basic document structure

Type this in `main.tex`:

```latex
\documentclass{article}

\title{My First LaTeX Document}
\author{Yujan Basnet}
\date{\today}

\begin{document}

\maketitle

\section{Introduction}
This is my first document written in LaTeX using Overleaf.

\section{Math Example}
Inline math: $a^2+b^2=c^2$  

Display math:
$$a^2+b^2=c^2$$

\end{document}
```

Click **Recompile** → your PDF appears on the right.

Since you prefer Obsidian/GitHub compatible math:

* Always use `$...$` for inline
* Always use `$$...$$` for display
* Never use `\[ ... \]` or `[ ... ]`

You are already following the correct exam-notes style.

Step 4: Common things you’ll use often

Sections:

```latex
\section{Title}
\subsection{Sub title}
```

Bold & italic:

```latex
\textbf{bold}
\textit{italic}
```

Lists:

```latex
\begin{itemize}
\item First point
\item Second point
\end{itemize}
```

Numbered list:

```latex
\begin{enumerate}
\item Step one
\item Step two
\end{enumerate}
```

New line:

```latex
\\
```

New paragraph: leave one empty line.

Step 5: Packages (for math-heavy notes)

At top, add:

```latex
\usepackage{amsmath, amssymb}
```

Full header becomes:

```latex
\documentclass{article}
\usepackage{amsmath, amssymb}
```

Step 6: Typical workflow in Overleaf

1. Write LaTeX in the middle
2. Click **Recompile**
3. See PDF instantly
4. Fix errors shown in red at bottom if any

---

For your exam notes style, your future documents will look like:

```latex
\section{Given}
...

\section{Formulas}
$$P(A|B)=\frac{P(A\cap B)}{P(B)}$$

\section{Step-by-step Solution}
1. Substitute values  
2. Simplify  

\section{Final Answer}
...
```
