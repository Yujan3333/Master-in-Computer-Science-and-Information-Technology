
## 1️⃣ Basic Table of Contents (Minimal)

Add this **where you want the ToC to appear** (usually after title page):

```latex
\tableofcontents
\newpage
```

That’s it ✅

---

## 2️⃣ Full Minimal Working Example

```latex
\documentclass{report}

\begin{document}

\tableofcontents
\newpage

\chapter{Introduction}
\section{Background}
\subsection{Motivation}

\chapter{Methodology}
\section{Data Collection}

\end{document}
```

👉 Compile **twice** (important)
• 1st run → collects headings
• 2nd run → displays ToC

---

## 3️⃣ What Automatically Appears in ToC?

| Command            | Appears in ToC |
| ------------------ | -------------- |
| `\chapter{}`       | ✅              |
| `\section{}`       | ✅              |
| `\subsection{}`    | ✅              |
| `\subsubsection{}` | ❌ (by default) |

---

## 4️⃣ Control Depth of Table of Contents

### Show up to subsection

```latex
\setcounter{tocdepth}{2}
```

### Show up to subsubsection

```latex
\setcounter{tocdepth}{3}
```

👉 Place **before** `\tableofcontents`

---

## 5️⃣ Unnumbered Sections in ToC (Important for Thesis)

If you use:

```latex
\section*{Acknowledgement}
```

❌ It will **NOT** appear in ToC.

### ✅ Correct Way (manual entry):

```latex
\section*{Acknowledgement}
\addcontentsline{toc}{section}{Acknowledgement}
```

For chapters:

```latex
\chapter*{Abstract}
\addcontentsline{toc}{chapter}{Abstract}
```

---

## 6️⃣ Roman Page Numbers for ToC (Thesis Standard)

```latex
\pagenumbering{roman}
\tableofcontents
\newpage
\pagenumbering{arabic}
```

Result:
• ToC → i, ii, iii
• Main content → 1, 2, 3

---

## 7️⃣ Separate Files (`\input`) — Works Perfectly

**main.tex**

```latex
\begin{document}

\tableofcontents
\newpage

\input{chapter1}
\input{chapter2}

\end{document}
```

**chapter1.tex**

```latex
\chapter{Introduction}
\section{Overview}
```

✔ ToC collects everything automatically

---

## 8️⃣ Common Problems & Fixes

❌ ToC empty
✔ Compile twice

❌ Page numbers wrong
✔ Add `\newpage` after `\tableofcontents`

❌ Acknowledgement not showing
✔ Use `\addcontentsline`

---

## 9️⃣ Recommended Order for Thesis

```latex
Title Page
Certificate
Acknowledgement
Abstract
\tableofcontents
List of Figures
List of Tables
Main Chapters
```

---
