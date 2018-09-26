`timescale 1ns / 1ps

module Execute(
input logic CLK,RESET,PCSrcE,NoWrite, RegWriteE, MemWriteE, BranchE, ALUSrcE, 
input logic [1:0] FlagsWriteE, ForwardAE, ForwardBE,
input logic [2:0] ALUControlE,
input logic [3:0] CondE, FlagsE, 
input logic [31:0] RD1E, RD2E, ExtImmE, ResultW, ALUResultM,
output logic [3:0] ALUFlagsEOut,
output logic PCSrcEOut, RegWriteEOut,BranchEOut, MemWriteEOut,
output logic [31:0] ALUResultE, WriteDataE
);

logic [31:0] SrcAE, SrcBE, mux32out; 
logic [3:0] ALUFlags;
//logic PCSrc,BrancheEout;

Mux3 #(.BITS(32)) mux31
(
.d0(RD1E),
.d1(ResultW), 
.d2(ALUResultM),
.s(ForwardAE),
.y(SrcAE));

Mux3 #(.BITS (32)) mux32
(
.d0(RD2E),
.d1(ResultW), 
.d2(ALUResultM),
.s(ForwardBE),
.y(mux32out)
);

Mux2 #(.BITS (32)) mux21
(
.d0(mux32out), 
.d1(ExtImmE),
.s(ALUSrcE),
.y(SrcBE)
);

ALU Alu(
.ALUControlE(ALUControlE),
.SrcAE(SrcAE), 
.SrcBE(SrcBE),
.ALUResultE(ALUResultE),
.ALUFlags(ALUFlags)
);


CondUnit CondUnit(

.CLK(CLK), 
.RESET(RESET),
.BranchEIn(BranchE),
.NoWrite(NoWrite),
.CondE(CondE),
.ALUFlags(ALUFlags),
.FlagsE(FlagsE),
.FlagWriteE(FlagsWriteE),
.ALUFlagsEOut(ALUFlagsEOut),
.PCSrcEIn(PCSrcE), 
.RegWriteEIn(RegWriteE), 
.MemWriteEIn(MemWriteE),
.PCSrcE(PCSrcEOut), 
.RegWriteE(RegWriteEOut), 
.BrancheE(BrancheEOut), 
.MemWriteE(MemWriteEOut)
);

//assign PCSrcEOut = BrancheE | PCSrcE;
assign WriteDataE = mux32out;

endmodule