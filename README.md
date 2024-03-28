<!-- TOC start (generated with https://github.com/derlin/bitdowntoc) -->

   * [🪄 Project Feature Breakdown](#-project-feature-breakdown)
- [:notebook_with_decorative_cover: Table of Contents](#notebook_with_decorative_cover-table-of-contents)
   * [:star2: About the Project](#star2-about-the-project)
      + [:camera: Screenshots](#camera-screenshots)
         - [Executing a file within the shell](#executing-a-file-within-the-shell)
         - [Using the interactive shell](#using-the-interactive-shell)
         - [Opening the github page](#opening-the-github-page)
   * [:toolbox: Installation (from PyPI or Build from Source)](#toolbox-installation-from-pypi-or-build-from-source)
      + [Build from Source](#build-from-source)
   * [:book: Usage Guide](#book-usage-guide)
   * [:wave: Contributing](#wave-contributing)
   * [:grey_question: FAQ](#grey_question-faq)
   * [:warning: License](#warning-license)

<!-- TOC end -->

<div align='center'>

<img src=https://github.com/vivekkdagar/xbasic/blob/main/assets/menu.png alt="logo"/>

<h1>xbasic</h1>
<p>A Python-based, extended interpretation of the BASIC language, enriched with additional features and functionalities.</p>

<h4> <span> · </span> <a href="https://github.com/vivekkdagar/xbasic/blob/master/README.md"> Documentation </a> <span> · </span> <a href="https://github.com/vivekkdagar/xbasic/issues"> Report Bug </a> <span> · </span> <a href="https://github.com/vivekkdagar/xbasic/issues"> Request Feature </a> </h4>


<br>

<!-- TOC --><a name="-project-feature-breakdown"></a>
## 🪄 Project Feature Breakdown
</div>

**Parsing and Tokenization:**
- Utilizes a custom lexical analyzer or tokenizer (`Token`, `TokenList`) to break down source code into tokens (keywords, identifiers, operators, literals).
- Implements parsing logic using recursive descent parsing.
- Recognizes the structure of the input code based on defined grammar rules.

**Abstract Syntax Tree (AST):**
- Defines classes (`Value`, `String`, `NumberNode`, `BinOpNode`, etc.) to represent nodes in the abstract syntax tree (AST).
- Constructs the AST by recursively building nodes during parsing.
  
**Error Handling:**
- Provides a `ParseResult` class to manage parsing results and errors.
- Defines error classes like `InvalidSyntaxError` and `RTError` for reporting syntax and runtime errors.

**Execution Logic:**
- Implements an interpreter component responsible for executing parsed AST nodes.
- Traverses the AST and performs operations defined by language semantics.

**Language Features:**
- Supports variables with data types such as numbers, strings, and lists.
- Provides constructs for control flow (`if`, `for`, `while` loops) and flow control statements (`return`, `continue`, `break`).
- Allows defining and calling functions (`func-def`, `call`).

**Utilities:**
- Tracks position (line and column numbers) of tokens and nodes in the source code using utilities like `Position`.
- Handles contextual information during parsing and execution using the `Context` class.
<br>

<!-- TOC --><a name="notebook_with_decorative_cover-table-of-contents"></a>
# :notebook_with_decorative_cover: Table of Contents

- [About the Project](#star2-about-the-project)
- [Installation & Usage Guide](#pypi)
- [Contributing](#wave-contributing)
- [FAQ](#grey_question-faq)
- [License](#warning-license)
- [Acknowledgements](#gem-acknowledgements)


<!-- TOC --><a name="star2-about-the-project"></a>
## :star2: About the Project

<!-- TOC --><a name="camera-screenshots"></a>
### :camera: Screenshots

<!-- TOC --><a name="executing-a-file-within-the-shell"></a>
#### Executing a file within the shell
<div align="center"> <a href=""><img src="https://github.com/vivekkdagar/xbasic/blob/main/assets/file.png" alt='image' width='800'/></a> </div>

<!-- TOC --><a name="using-the-interactive-shell"></a>
#### Using the interactive shell
<div align="center"> <a href=""><img src="https://github.com/vivekkdagar/xbasic/blob/main/assets/shell.png" alt='image' width='800'/></a> </div>

<!-- TOC --><a name="opening-the-github-page"></a>
#### Opening the github page
<div align="center"> <a href=""><img src="https://github.com/vivekkdagar/xbasic/blob/main/assets/git.png" alt='image' width='800'/></a> </div>



<!-- TOC --><a name="toolbox-installation-from-pypi-or-build-from-source"></a>
## :toolbox: Installation (from PyPI or Build from Source)



<h3><a id="pypi"> Install from PyPI</a></h3>

You can install the `xbasic` package directly from PyPI using the following command:

```bash
pip install xbasic
```


<!-- TOC --><a name="build-from-source"></a>
### Build from Source

Clone the repository

```bash
git clone https://github.com/vivekkdagar/xbasic
```

Go to the project directory
```bash
cd xbasic
```

Build the package:

```bash
python3 -m build
```

Install the package:

```bash
pip install dist/*gz
```

<!-- TOC --><a name="book-usage-guide"></a>
## :book: Usage Guide

Below is a guide on how to interact with xbasic:

1. **Open github page**
   ```bash
     xbasic report
   ```


2. **Start an interactive shell**

   ```bash
     xbasic shell
   ```

3. **Execute a file within the shell**

   ```bash
     xbasic file -f path
   ```
   
   - `-f`: Specify the path where the bsx file is.




<!-- TOC --><a name="wave-contributing"></a>
## :wave: Contributing

<a href="https://github.com/vivekkdagar/xbasic/graphs/contributors"> <img src="https://contrib.rocks/image?repo=Louis3797/awesome-readme-template" /> </a>

Contributions are always welcome!

see `contributing.md` for ways to get started

<!-- TOC --><a name="grey_question-faq"></a>
## :grey_question: FAQ

**1. What is XBasic?**
   - XBasic is a project aimed at developing an interpreter for a programming language called XBasic. It involves the creation of a parser, lexer, and executor for XBasic code, allowing users to write and execute XBasic programs.

**2. What features does XBasic offer?**
   - XBasic aims to provide a range of features common to programming languages, including variable assignment, arithmetic operations, control flow statements (such as if-else, loops), function definitions, and function calls. It also supports data types like numbers, strings, and lists.

**3. How is XBasic implemented?**
   - XBasic is implemented in Python. The project includes custom logic for lexical analysis (tokenization), parsing, and execution of XBasic code. It utilizes object-oriented programming principles to represent language constructs and manage program execution.

**5. How are errors handled in XBasic?**
   - XBasic includes error handling mechanisms to report syntax errors during parsing and runtime errors during program execution. Custom error classes are used to provide informative messages, including error location and context, helping users debug their code effectively.

**6. How can I get started with XBasic?**
   - To get started with XBasic, you can clone the project repository from GitHub and follow the setup instructions. Once set up, you can explore the codebase, contribute to development, or use the interpreter to write and execute XBasic programs. Additionally, documentation and examples are provided to guide users through usage and development processes.

**7. What file format does XBasic use?**
   - XBasic uses the ".bsx" file format for XBasic source code files. Users can write XBasic code in files with the ".bsx" extension, and the XBasic interpreter can parse and execute these files. This file format helps organize and store XBasic programs efficiently.



<!-- TOC --><a name="warning-license"></a>
## :warning: License

Distributed under the MIT License. See LICENSE for more information.
