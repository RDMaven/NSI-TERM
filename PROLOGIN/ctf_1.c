
/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Instruction at (ram,0x0010132e) overlaps instruction at (ram,0x0010132b)
    */

undefined8 FUN_00101209(void)

{
  int iVar1;
  size_t sVar2;
  char *pcVar3;
  long lVar4;
  long unaff_RBP;
  undefined8 *puVar5;
  long in_FS_OFFSET;
  char cVar6;
  bool bVar7;
  byte bVar8;
  undefined8 local_418;
  undefined8 local_410;
  undefined8 local_408 [127];
  long local_10;
  
  bVar8 = 0;
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  getenv("LINES");
  getenv("COLUMNS");
  puts("Enter your Serial: ");
  local_418 = 0;
  local_410 = 0;
  puVar5 = local_408;
  for (lVar4 = 0x7e; lVar4 != 0; lVar4 = lVar4 + -1) {
    *puVar5 = 0;
    puVar5 = puVar5 + (ulong)bVar8 * -2 + 1;
  }
  iVar1 = __isoc99_scanf("%1024s",&local_418);
  bVar8 = (byte)lVar4;
  fflush(stdin);
  if (iVar1 != -1) {
    syscall();
    sVar2 = strlen((char *)&local_418);
    iVar1 = FUN_0010142e(&local_418,sVar2);
    if (iVar1 == 0) {
      LOSE();
    }
    else {
      WIN();
    }
    cVar6 = '\0';
    bRam0000000000000001 = bRam0000000000000001 & bVar8;
    bVar7 = bRam0000000000000001 == 0;
    pcVar3 = (char *)(**(code **)(unaff_RBP + -0x3f00b762))();
    if (!bVar7) {
      if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
        __stack_chk_fail();
      }
      return 0;
    }
    *pcVar3 = *pcVar3 + bVar8 + cVar6;
                    /* WARNING: Bad instruction - Truncating control flow here */
    halt_baddata();
  }
                    /* WARNING: Subroutine does not return */
  exit(1);
}


/* WARNING: Control flow encountered bad instruction data */

void FUN_0010142e(undefined8 param_1,long param_2)

{
  long in_FS_OFFSET;
  
  if (param_2 == 0x19) {
                    /* WARNING: Call to offcut address within same function */
    func_0x0010145d();
                    /* WARNING: Bad instruction - Truncating control flow here */
    halt_baddata();
  }
  if (*(long *)(in_FS_OFFSET + 0x28) == *(long *)(in_FS_OFFSET + 0x28)) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

