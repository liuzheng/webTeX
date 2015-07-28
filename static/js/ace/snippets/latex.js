define("ace/snippets/latex",["require","exports","module"], function(require, exports, module) {
"use strict";

exports.snippetText ="# documentclass\n\
snippet documentclass\n\
	documentclass[${1?:12pt,a4paper}]\{${2:book}\} \n\
	${3?:body}\n\
# begin\n\
snippet begin\n\
	begin\{${1?:function_name}\}[${2:argument}] \n\
		${3:}\n\
	\\end\{${1}\}\n\";\
# begin{\n\
snippet begin{\n\
	begin\{${1?:function_name}\}[${2:argument}] \n\
		${3:}\n\
	\\end\{${1}\}\n\";\
	";
exports.scope = "latex";

});
