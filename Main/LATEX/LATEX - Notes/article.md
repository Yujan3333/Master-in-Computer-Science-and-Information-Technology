`\documentclass{article}` tells LaTeX what *type of document* you are creating.
It is like selecting a template or category.

Think of it as:

> “I am writing an **article-style** document.”

Different document classes change:

* Page layout
* Title style
* Section formatting
* Font sizing rules
* Default structure

Common classes:

| Class     | Used for                                                 |
| --------- | -------------------------------------------------------- |
| `article` | Seminar papers, assignments, short reports (most common) |
| `report`  | Long reports, theses (has chapters)                      |
| `book`    | Books (chapters, parts, front matter)                    |
| `beamer`  | Presentations (slides)                                   |

So when you write:

```latex
\documentclass[11pt]{article}
```

it means:

* Use the **article** format
* Set base font size to **11 pt**

For your seminar:

* You don’t need chapters
* You only need sections and subsections
  So `article` is the *correct* and *simplest* choice.

Internally, `article`:

* Defines `\section`, `\subsection`, `\subsubsection`
* Uses single-column layout by default
* Starts numbering from Section 1
* Keeps formatting academic-paper style

If you used:

```latex
\documentclass{report}
```

Then LaTeX would expect:

```latex
\chapter{...}
```

which you *don’t* want for a seminar.

So:

> `\documentclass{article}` =
> “Create a normal academic paper layout suitable for seminars, assignments, and short research papers.”
