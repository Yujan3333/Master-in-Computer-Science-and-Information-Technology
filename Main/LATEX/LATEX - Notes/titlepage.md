
```md

% Title Page Starts
\begin{titlepage}
    \begin{center}
        
        % Set line spacing to 1.5 for the title page
        \setstretch{1.5}
        
        %------------------------------------------------
        % University and Institute Name
        %------------------------------------------------
        \textbf{\large TRIBHUVAN UNIVERSITY} \\
        \textbf{\large Institute of Science and Technology}
        
        \vspace{0.8cm}  % Vertical space
        
        % University Logo
        \includegraphics[width=0.35\textwidth]{images/TU LOGO.jpg} 
        
        \vspace{1.5cm}
        
        % Seminar Title
        \textbf{\large Seminar Report} \\
        \textbf{\large On} \\
        \textbf{\large ``Nepali Sentiment Analysis''}
        
        \vfill  % Pushes the following content towards bottom
        
        % Submitted To Section
        \textbf{Submitted to:} \\
        \textbf{Central Department of Computer Science and Information Technology} \\
        \textbf{Tribhuvan University, Kritipur} \\
        \textbf{Kathmandu, Nepal}
        
        \vspace{1cm}
        
        % Submitted By Section
        \textbf{Submitted by:} \\
        \textbf{Yujan Basnet} \\
        \textbf{Roll No. 18/081}
        
        \vfill
        
        % Degree and Semester Information
        \textbf{In partial fulfillment of the requirement for Master's Degree in Computer Science and Information Technology (M.Sc. CSIT)} \\
        \textbf{Second Semester} \\
        \textbf{\monthname[\month] \the\year}
        
    \end{center}
\end{titlepage}

```


---
## Explanation
```latex
%----------------------------------------------------
% Title Page Content
%----------------------------------------------------
```

This is just a **comment**. LaTeX ignores it. It is only for humans to understand the code.

---

```latex
\begin{titlepage}
```

Starts a special page that is treated as a **title page**.
LaTeX will:

* Put it on its own page
* Not number it
* Format it separately from the rest of the document

---

```latex
\begin{center}
```

Everything inside this will be **center aligned horizontally**.

---

```latex
\setstretch{1.5}
```

Sets **line spacing** to 1.5 for the title page (using the `setspace` package).
Makes it look similar to Word formatting.

---

```latex
\textbf{\large TRIBHUVAN UNIVERSITY} \\
```

* `\textbf{}` → makes text **bold**
* `\large` → increases font size
* `\\` → forces a **new line**

Same logic for:

```latex
\textbf{\large Institute of Science and Technology}
```

---

```latex
\vspace{0.8cm}
```

Adds **vertical space** of 0.8 cm between text blocks.

---

```latex
\includegraphics[width=0.35\textwidth]{tu_logo.png}
```

* `\includegraphics` → inserts an image
* `width=0.35\textwidth` → image is 35% of page width
* `{tu_logo.png}` → file name of the image

Your logo must be in the same folder as `.tex` file.

---

```latex
\vspace{1.5cm}
```

Adds more space after the logo.

---

```latex
\textbf{\large Seminar Report} \\
\textbf{\large On} \\
```

Three bold, large-sized lines.

---

```latex
\textbf{\large ``Comparative Study of Multinomial and Bernoulli Na\"ive Bayes for Nepali Sentiment Analysis''}
```

* Double backticks `` and '' produce proper quotation marks
* `\"i` in `Na\"ive` produces the ï in *Naïve*

---

```latex
\vfill
```

This is powerful:

* It pushes all following content **towards the bottom** of the page
* Used to vertically balance the page layout

---

```latex
\textbf{Submitted to:} \\
```

Bold heading for the next block.

Then:

```latex
\textbf{Central Department of Computer Science and Information Technology} \\
\textbf{Tribhuvan University, Kritipur} \\
\textbf{Kathmandu, Nepal}
```

Each line bold, each line broken with `\\`.

---

```latex
\vspace{1cm}
```

Small gap before the next section.

---

```latex
\textbf{Submitted by:} \\
```

Label.

```latex
\textbf{Yujan Basnet} \\
\textbf{Roll No. 18/081}
```

Your name and roll number.

---

```latex
\vfill
```

Again pushes the final block to the bottom.

---

```latex
\textbf{In partial fulfillment of the requirement for Master's Degree in Computer Science and Information Technology (M.Sc. CSIT)} \\
\textbf{First Semester} \\
\textbf{September 2025}
```

Final academic information:

* Degree requirement line
* Semester
* Submission date

---

```latex
\end{center}
```

Ends center alignment.

---

```latex
\end{titlepage}
```

Ends the title page environment.

LaTeX now:

* Finishes the title page
* Starts a new normal page for your content

---

In short:

| Command             | Purpose                        |
| ------------------- | ------------------------------ |
| `% ...`             | Comment                        |
| `\begin{titlepage}` | Create a special title page    |
| `\begin{center}`    | Center everything              |
| `\setstretch{1.5}`  | 1.5 line spacing               |
| `\textbf{}`         | Bold text                      |
| `\large`            | Increase font size             |
| `\\`                | New line                       |
| `\vspace{}`         | Fixed vertical space           |
| `\vfill`            | Flexible space to push content |
| `\includegraphics`  | Insert image                   |
| `\end{center}`      | Stop centering                 |
| `\end{titlepage}`   | End title page                 |



---
---
## Output
![](../../../Images/Second_Sem_Images/titlepage-pdf.pdf)