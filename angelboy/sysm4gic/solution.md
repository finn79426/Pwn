進入 GDB 後，disas get_flag
找到 if(password == magic) 這一行的反組譯碼 cmp rdx, rax
找到該指令的記憶體位置，對它下段點 b *0x4007c4
run 程式，然後隨意輸入。例如：4207849484 (0xfaceb00c)
set $rax=$rdx
context 確認暫存器有被我們修改
contineu

FLAG：AIS3{d3bugger_1s_v3ry_us3ful_isn7}
