
```md
%--------------------------------------
% Supervisor Recommendation
% -------------------------------------
\thispagestyle{empty} % Forces this specific page to have no number
\begin{center}
    \includegraphics[width=0.2\textwidth]{images/TU LOGO.jpg} \\[0.5cm]
    {\large \textbf{Tribhuvan University}} \\[0.2cm]
    {\large \textbf{Institute of Science and Technology}} \\[1.5cm]
    
    {\Large \textbf{SUPERVISOR RECOMMENDATION}} \\[1cm]
\end{center}

\noindent This is to certify that Mr. Yujan Basnet (Roll No. 18/081) has submitted the seminar report on the topic \textbf{“ TOPIC ?? Nepali Sentiment Analysis”} for the partial fulfillment of Master’s of Science in Computer Science and Information Technology, Second semester. I hereby, declare that this seminar report has been approved.

\vspace{3cm}

\noindent \rule{5cm}{0.4pt} \\
\textbf{Supervisor} \\
Asst. Prof. Mr. Jagdish Bhatta \\
Central Department of Computer Science and Information Technology
\newpage


%--------------------------------------
% Letter of Approval
% -------------------------------------
\thispagestyle{empty} % Forces this specific page to have no number

\begin{center}
    {\Large \textbf{LETTER OF APPROVAL}} \\[1cm]
\end{center}

\noindent This is to certify that the seminar report prepared by Mr. Yujan Basnet entitled \textbf{“TOPIC ??? Nepali Sentiment Analysis”} in partial fulfillment of the requirements for the degree of Master’s of Science in Computer Science and Information Technology has been well studied. In our opinion, it is satisfactory in the scope and quality as a project for the required degree.

\vspace{1.5cm}
\begin{center}
    \textbf{Evaluation Committee}
\end{center}
\vspace{4cm}

\noindent
\begin{minipage}{0.45\textwidth}
    \rule{5cm}{0.4pt} \\
    \textbf{Asst. Prof. Sarbin Sayami} \\
    (H.O.D) \\
    Central Department of CSIT
\end{minipage}

\hfill   % "horizontal spring" that pushes content apart to fill the entire width of the line.

\begin{minipage}{0.45\textwidth}
    \rule{5cm}{0.4pt} \\
    \textbf{Asst. Prof. Jagdish Bhatta} \\
    (Supervisor) \\
    Central Department of CSIT
\end{minipage}

\vspace{4cm}

\begin{center}
    \rule{5cm}{0.4pt} \\
    (Internal)
\end{center}
\newpage


%--------------------------------------
% Acknowledgement
% -------------------------------------
\pagenumbering{roman} % Start i, ii, iii...
\setcounter{page}{1}  % Force it to start at i
\pagestyle{plain}     % Show the page number at the bottom center

\begin{center}
    {\Large \textbf{ACKNOWLEDGEMENT}} \\[1cm]
\end{center}

\noindent I am sincerely grateful to everyone who supported me throughout the completion of this report. I would like to thank my supervisor, \textbf{Asst. Prof. Jagdish Bhatta}, for his guidance, encouragement, and valuable advice, which kept me motivated and on track.

\noindent I am also thankful to \textbf{Asst. Prof. Sarbin Sayami}, Head of the Central Department of Computer Science and Information Technology, for his helpful insights and constant support. I would like to express my gratitude to the Central Department of Computer Science and Information Technology, Tribhuvan University, and all its faculty members for providing a platform to explore and learn.

\noindent Finally, I am thankful to my friends and everyone who helped me, directly or indirectly, during this journey. Your support and encouragement have been truly appreciated.

\vspace{2cm}

\begin{flushright}
    \textbf{Yujan Basnet} \\
    \textbf{Roll No: 18/081}
\end{flushright}
\newpage
```


---
## Explanation
Sure! Let’s go through your LaTeX code **step by step** and explain every key keyword, command, and environment you used. I’ll explain it in a way that’s clear for document preparation purposes.

---

## **1. `\thispagestyle{empty}`**

* **Purpose:** Removes page numbers and headers/footers from **this page only**.
* **Used in:** Supervisor Recommendation and Letter of Approval.
* **Why:** These pages in academic documents usually should **not have page numbers**.

---

## **2. `\begin{center} ... \end{center}`**

* **Purpose:** Centers all content inside this environment horizontally.
* **Used in:** Titles, logos, and main headings.
* **Example:**

```latex
\begin{center}
    {\Large \textbf{SUPERVISOR RECOMMENDATION}}
\end{center}
```

* Makes the text appear **centered** on the page.

---

## **3. `\includegraphics[width=0.2\textwidth]{images/TU LOGO.jpg}`**

* **Purpose:** Inserts an image (like a logo).
* **Options:**

  * `width=0.2\textwidth` → sets the image width to 20% of the text width.
* **Used in:** Displaying the university logo at the top.
* **Important:** Requires `\usepackage{graphicx}` in your preamble.

---

## **4. Font size commands: `\large`, `\Large`**

* **Purpose:** Adjusts the size of the text.

  * `\large` → slightly larger than normal.
  * `\Large` → bigger than `\large`.
* **Used in:** Titles and headings.

---

## **5. `\textbf{...}`**

* **Purpose:** Makes the text **bold**.
* **Used in:** University name, headings, supervisor names.

---

## **6. `\\[0.5cm]` or `\\[1cm]`**

* **Purpose:** Inserts a **line break** with **extra vertical space**.
* **Example:**

```latex
\\[0.5cm]  % Break line + 0.5cm vertical space
```

* Useful for spacing between logo, title, and other text.

---

## **7. `\noindent`**

* **Purpose:** Prevents LaTeX from **indenting the first line** of the paragraph.
* **Used in:** The main text of Supervisor Recommendation, Letter of Approval, Acknowledgement.

---

## **8. `\vspace{3cm}`**

* **Purpose:** Adds **vertical space** of the specified height.
* **Example:** `\vspace{3cm}` → adds 3 cm of blank space.
* **Used in:** Creating space before signatures or at the bottom of the page.

---

## **9. `\rule{5cm}{0.4pt}`**

* **Purpose:** Draws a **horizontal line**.
* **Parameters:**

  * First → width (5 cm).
  * Second → thickness (0.4 pt).
* **Used in:** Signatures and separating sections.

---

## **10. `\newpage`**

* **Purpose:** Forces a **page break**, starting a **new page**.
* **Used in:** After each main section like Supervisor Recommendation, Letter of Approval, Acknowledgement.

---

## **11. `\begin{minipage}{0.45\textwidth} ... \end{minipage}`**

* **Purpose:** Creates a **box/mini page** that can hold text or other elements.
* **Width:** 45% of the text width (`0.45\textwidth`).
* **Used in:** Placing **two signature lines side by side** (Evaluation Committee).
* **Important:** Combine with `\hfill` to **separate boxes horizontally**.

---

## **12. `\hfill`**

* **Purpose:** Inserts a **flexible horizontal space**.
* **Used in:** Pushing two `minipage`s apart so they align on left and right side.

---

## **13. `\pagenumbering{roman}`**

* **Purpose:** Changes page numbering to **roman numerals** (i, ii, iii…).
* **Used in:** Front matter (Acknowledgement, Abstract, Table of Contents).

---

## **14. `\setcounter{page}{1}`**

* **Purpose:** Forces the **page number to start at a specific number**.
* **Used in:** Acknowledgement, starting numbering at `i`.

---

## **15. `\pagestyle{plain}`**

* **Purpose:** Sets the **style of page numbers**.

  * `plain` → page numbers appear at the **bottom center**.
* **Used in:** Acknowledgement and other front matter after initial pages with no numbers.

---

## ✅ Summary of flow in your code:

1. **Supervisor Recommendation**

   * No page number → `\thispagestyle{empty}`
   * Logo + centered title + text + signature

2. **Letter of Approval**

   * No page number → `\thispagestyle{empty}`
   * Centered heading + evaluation committee signatures side by side

3. **Acknowledgement**

   * Roman page numbers → `\pagenumbering{roman}` + start at i
   * Plain style → `\pagestyle{plain}`
   * Centered heading + main text + author signature

---
