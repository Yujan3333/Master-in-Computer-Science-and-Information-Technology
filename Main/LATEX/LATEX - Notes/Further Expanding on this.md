
## 1️⃣ Folder structure

```
project/
│
├── main.tex
├── titlepage.tex
├── frontmatter.tex   % supervisor recommendation + acknowledgement
├── abstract.tex
├── toc.tex           % table of content, figures, tables
├── body.tex          % introduction → conclusion
├── references.tex
├── appendix.tex      % code, extra stuff
└── images/           % all images
```

---

## 2️⃣ main.tex skeleton

```latex
\documentclass[12pt,a4paper]{report} % report is better for chapters

% Packages
\usepackage[utf8]{inputenc}
\usepackage{graphicx}
\usepackage{setspace}
\usepackage{geometry}
\usepackage{tocbibind} % adds TOC, LOF, LOT to TOC automatically

\geometry{margin=1in}

\begin{document}

%-----------------------------
% TITLE PAGE
%-----------------------------
\input{titlepage}

%-----------------------------
% FRONT MATTER (Supervisor + Acknowledgement)
% Page numbering: i, ii, ...
%-----------------------------
\pagenumbering{roman} % start Roman numerals
\setcounter{page}{1}  % start from i
\input{frontmatter}

%-----------------------------
% ABSTRACT
% Continue Roman numerals
%-----------------------------
\input{abstract}

%-----------------------------
% TABLE OF CONTENTS, FIGURES, TABLES
% Roman numerals continued
%-----------------------------
\input{toc}

%-----------------------------
% MAIN BODY
% Page numbering: Arabic 1,2,3 ...
%-----------------------------
\clearpage
\pagenumbering{arabic} % start Arabic numbering
\setcounter{page}{1}   % start from 1
\input{body}

%-----------------------------
% REFERENCES
% continues Arabic numbering
%-----------------------------
\input{references}

%-----------------------------
% APPENDIX / CODE / EXTRA
%-----------------------------
\input{appendix}

\end{document}
```

---

## 3️⃣ Key things to make your numbering correct

1. **Front matter:**

```latex
\pagenumbering{roman} % i, ii, iii
\setcounter{page}{1}  % start at i
```

All your front pages (acknowledgement, recommendation, abstract, TOC) go here.

2. **Main matter:**

```latex
\clearpage
\pagenumbering{arabic} % 1,2,3...
\setcounter{page}{1}   % start main chapters
```

* `\clearpage` ensures a page break before numbering changes.
* Main body (Introduction → Conclusion) now starts at **1**.

3. **TOC / List of Figures / Tables:**
   Include them in one file:

```latex
\tableofcontents
\listoffigures
\listoftables
```

* This will automatically pick up Roman numbering if you are still in `\pagenumbering{roman}`.

---

## 4️⃣ Notes on your specific concern

> "the page number (i) starts from acknowledgement"

✅ Correct: Front matter (acknowledgement, supervisor letter, abstract, TOC) **all share Roman numerals**. Title page is usually **unnumbered**, which is fine (`\maketitle` or your `titlepage` environment does this).

> "page no starts from 1 2 3 .. here" for main body

✅ Correct: Use `\pagenumbering{arabic}` at the start of your main content.

---

## 5️⃣ Recommended tweaks

* Use `report` class instead of `article` if you want chapters and better front-matter handling.
* Wrap front matter in a separate file (`frontmatter.tex`) and main body in `body.tex` for clarity.
* Use `\appendix` before appendix/code sections if you want labels like `Appendix A`, `Appendix B`.

---

### ✅ Conclusion

Your plan is **completely feasible** and actually the standard way to structure:

1. Title page → unnumbered
2. Supervisor/acknowledgement → Roman numerals i, ii
3. Abstract → continue Roman
4. TOC/LOF/LOT → continue Roman
5. Main body → Arabic numbering starts at 1
6. References → continue Arabic
7. Appendix/extra → continue Arabic

---
