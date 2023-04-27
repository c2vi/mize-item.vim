if !has('python3')
    echomsg ':python3 is not available, mize-item.vim will not be loaded.'
    finish
endif

command! -nargs=1 I call s:Load_item(<f-args>)


function s:Load_item(...)
"let ind = index(argv(), "-i")
"if ind >= 0
	"if len(argv()) <= ind +1
		"echo "No ID provided to open an mize-item"
		"finish
	"endif
	"let tmp_id = argv()[ind +1]
	"let tmp_id = "0"

	cnoreabbrev q q!
	set noswapfile
	python3 from open_item import *
	"python3 print("hello")
	autocmd VimLeavePre * python3 terminate_thread()
	autocmd BufWriteCmd * python3 update_item()
	python3 open_item(vim.eval("a:1"))
	set syntax=json

"endif
endfunction

