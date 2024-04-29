##Assignment 7 Code generation

##Information on generating WAT code from source code in kulant  
File AST.py contains the code that converts the   
given source code in our custom language 'kulant' to Web Assembly Text (WAT).   

You can generate both AST and WAT file by running the AST.py.   
If you want to run only the code for WAT generation you would have to comment out the AST code generation  
since it has more dependencies on several heavy python packages like graphviz.   
   
To run AST.py, go to the terminal and run the command   
$ python3 AST.py  
   
This would generate .wat file.   
   
##Information about getting WASM files   
Now you would have to install wat2wasm toolkit to convert these .wat files to .wasm files which are used to run test case. Once you have installed the wat2wasm toolkit using the instructions from the website <https://github.com/WebAssembly/wabt>, use the command    
$ wat2wasm <name of wat file> -o <name of wasm file>.    
   
##Information about keeping files in same directory   
1. Please ensure the following files are in the same folder   
		1.1 AST_final.py   
		1.2 ast_classes.py   
		1.3 gram_file.txt   
		1.4 folder source code files files in kulant
			1. 4.1 arithmetic,kul   
			1.4.2 caesar.kul   
			1.4.3 sort.kul   
		1.5 AST.py   
		1.6 code_generation.py   
		1.7 Semantic_analyser.py   
   
   
##Other files in directory   
1. Folder named ‘WAT files’ contains the file generated for the four cases mentioned in the assignment   
		1.1 arithmetic.wat   
		1.2 caesar.wat   
		1.3 sort.wat   
2. 1. Folder named ‘WASM files’ contains the file generated for the four cases mentioned in the assignment   
		1.1 arithmetic.wasm    
		1.2 caesar.wasm   
		1.3 sort.wasm   
