`timescale 1ns / 1ps

module CondUnit(
input logic CLK, RESET, PCSrcEIn, RegWriteEIn, MemWriteEIn,BranchEIn,NoWrite,
input logic [1:0] FlagWriteE,
input logic [3:0] CondE,FlagsE,ALUFlags,

output logic [3:0] ALUFlagsEOut,
output logic PCSrcE, RegWriteE, BranchE, MemWriteE
);

logic [1:0] FlagW;
logic [3:0] Flags;
logic CondExE;


Flopr #(2)flagreg1(CLK, RESET, FlagW[1],FlagsE[3:2], Flags[3:2]);

Flopr #(2)flagreg0(CLK, RESET, FlagW[0],FlagsE[1:0], Flags[1:0]);

condcheck cc(CondE, Flags, CondExE);

assign FlagW = FlagWriteE & {2{CondExE}};
assign RegWriteE = RegWriteEIn & CondExE & ~NoWrite;//CMP--
assign MemWriteE = MemWriteEIn & CondExE;
assign PCSrcE = PCSrcEIn & CondExE;
assign BranchE = BranchEIn & CondExE;
assign ALUFlagsEOut = ALUFlags;

endmodule


module condcheck(


input logic [3:0] CondE,
input logic [3:0] Flags,
output logic CondExE);


logic neg, zero, carry, overflow, ge;
assign {neg, zero, carry, overflow} = Flags;
assign ge = (neg == overflow);

always_comb

case(CondE)
4'b0000: CondExE = zero; // EQ
4'b0001: CondExE = ~zero; // NE
4'b0010: CondExE = carry; // CS
4'b0011: CondExE = ~carry; // CC
4'b0100: CondExE = neg; // MI
4'b0101: CondExE = ~neg; // PL
4'b0110: CondExE = overflow; // VS
4'b0111: CondExE = ~overflow; // VC
4'b1000: CondExE = carry & ~zero; // HI
4'b1001: CondExE = ~(carry & ~zero); // LS
4'b1010: CondExE = ge; // GE
4'b1011: CondExE = ~ge; // LT
4'b1100: CondExE = ~zero & ge; // GT
4'b1101: CondExE = ~(~zero & ge); // LE
4'b1110: CondExE = 1'b1; // Always
default: CondExE = 1'bx; // undefined

endcase

endmodule