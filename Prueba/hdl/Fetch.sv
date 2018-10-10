`timescale 1ns / 1ps

module Fetch #(parameter BITS = 32) (
	input logic [BITS-1:0] ALUSResultE, ResultW,
	input logic CLK,PCSrcW,BranchE,StallF,RESET,
	output logic [BITS-1:0] InstrF, PCPlus4F);

	logic [BITS-1:0] PC,PCF,MuxCon;
	
	
	RegPC RegPC(
		.pcIn(PC),
		.stall(StallF),
		.CLK(CLK),
		.RESET(RESET),
		.pcOut(PCF)
	);	

	Mux2 mux2EntradaF1(
		.d0(PCPlus4F),
		.d1(ResultW),
		.s(PCSrcW),
		.y(MuxCon));

	Mux2 mux2EntradaF2(
		.d0(MuxCon),
		.d1(ALUSResultE),
		.s(BranchE),
		.y(PC));

	InstructionMemory MemoriaInst(
		.a(PCF),
		.rd(InstrF));

	Adder #(.WIDTH(32)) Sumador(
		.a(PCF),
		.b(32'd4),
		.PCPlus4F(PCPlus4F));

endmodule