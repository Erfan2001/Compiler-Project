# Compiler Analysis Project 

## Project description:

The primary objective of this project is to develop a basic C language compiler, excluding functionalities for input capture and output display.

The initial phase, which may also encompass the second phase, focuses on lexical analysis. This phase takes the program string as input and yields an array of tokens as output. It's imperative to utilize the previous phase's output as input, implementing this stage potentially through DFA (Deterministic Finite Automaton). When working in a group, collaboration in this step is essential, with the inclusion of the DFA as a documented reference.

Following lexical analysis, the subsequent compiler phase is syntax analysis. Here, the previous phase's output serves as input, resulting in the generation of a Parse tree. If working individually, this phase can be accomplished through a single file, where input text is received, and prior-phase correctness isn't mandatory. To commence this phase, you must formulate a simple grammar and choose between various parsing methods, including bottom-up and top-down parsing, as detailed in the professor's explanations. The output of this phase, a tree, may differ from the initially designed grammar.

The subsequent phase entails semantic analysis of the Parse tree generated in the previous phase. Here, the objective is to identify and report semantic errors within the tree, providing appropriate error messages when necessary. Successful completion of this phase signifies the absence of errors in the preceding phases and allows for the tree to be printed. However, the detection of operations like adding two strings and storing the result in an integer variable should trigger error reporting.

The fifth stage involves the production of intermediary code.

The sixth stage pertains to optimization.

The seventh and final stage focuses on generating machine code. Notably, assembly language is machine-dependent, whereas C language is machine-independent. Thus, executing a C language program on a machine with unique specifications necessitates the development of a new compiler.

## Team members & files:

Team Members 😎:
* Seyed Erfan Nourbakhsh 983613059
* Seyed Amin Hossaini 983623012
* Mohammad Matin Leis Saffar 983623027
* Negar Barooti 983613007

Master: Ms.Zojaji

Presentation Link: https://drive.google.com/file/d/15wRuGV95t8c1Q6kel-pGn-paAf-CX2rt/view

# Result:

Overview: Generally our project is based on Python code.
The project is divided into 5 Phases including:
1. Pre Processing
2. Lexical Analyzer
3. Syntax Analyzer
4. Semantic Analyzer
5. Code Generation

Fall 2021
