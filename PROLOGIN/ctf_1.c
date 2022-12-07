
/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Instruction at (ram,0x0010132e) overlaps instruction at (ram,0x0010132b)
    */

def main():

{
  int iVar1;
  int extraout_EAX;
  size_t input_length;
  char *pcVar2;
  long i;
  long unaff_RBP;
  undefined8 *puVar3;
  long in_FS_OFFSET;
  char cVar4;
  bool boolean;
  int bVar5;
  char user_input;
  undefined8 local_410;
  undefined8 local_408 [127];
  long local_10;
  
  bVar5 = 0;
  local_10 = *(long *)(in_FS_OFFSET + 40);
  //getenv("LINES");
  //getenv("COLUMNS");
  puts("Enter your Serial: ");
  _user_input = 0;
  local_410 = 0;
  puVar3 = local_408;
  *puVar3 = 0;

  iVar1 = __isoc99_scanf("%1024s",&user_input);
  bVar5 = 0;
  fflush(stdin);
  if (iVar1 != -1) {
    syscall();
    input_length = strlen(&user_input);
    if (extraout_EAX == 0) {
      loose();
    }
    else {
      win();
    }
  }
   
  /* cVar4 = '\0';
    boolean = False;
    pcVar2 = (char *)(**(code **)(unaff_RBP + -0x3f00b762))();
    if (!boolean) {
      if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    WARNING: Subroutine does not return
        __stack_chk_fail();
      }
      return 0;
    }
    *pcVar2 = *pcVar2 + 0 + '\0';
                     WARNING: Bad instruction - Truncating control flow here    halt_baddata();
  }
                     WARNING: Subroutine does not return
              
  exit(1);
  */
}

