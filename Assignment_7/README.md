## Assignment 7: Code Generation

### Information on Generating WAT Code from Source Code in Kulant

File `AST.py` contains the code that converts the given source code in our custom language 'Kulant' to Web Assembly Text (WAT).

You can generate both AST and WAT files by running `AST.py`. If you want to run only the code for WAT generation, you would have to comment out the AST code generation since it has more dependencies on several heavy Python packages like Graphviz.

To run `AST.py`, go to the terminal and run the command:
  
`$ python3 AST.py`
   

This would generate a `.wat` file.

### Information about Getting WASM Files

Now you would have to install `wat2wasm` toolkit to convert these `.wat` files to `.wasm` files, which are used to run test cases. Once you have installed the `wat2wasm` toolkit using the instructions from the website [WebAssembly/wabt](https://github.com/WebAssembly/wabt), use the command:

 
`$ wat2wasm <name of wat file> -o <name of wasm file>.` 
   

### Information about Keeping Files in the Same Directory

1. Please ensure the following files are in the same folder:
   1. `AST_final.py`
   2. `ast_classes.py`
   3. `gram_file.txt`
   4. Folder `source_code_files` in Kulant
      1. `arithmetic.kul`
      2. `caesar.kul`
      3. `sort.kul`
   5. `AST.py`
   6. `code_generation.py`
   7. `Semantic_analyser.py`

### Other Files in Directory

1. Folder named `WAT files` contains the file generated for the four cases mentioned in the assignment:
   1. `arithmetic.wat`
   2. `caesar.wat`
   3. `sort.wat`
2. Folder named `WASM files` contains the file generated for the four cases mentioned in the assignment:
   1. `arithmetic.wasm`
   2. `caesar.wasm`
   3. `sort.wasm`
