.8086
.model tiny
.code
ORG 100h
START:
message db 'Hello,world!$'
mov ah, 9h
mov dx, offset message
int 21h
ret

end START