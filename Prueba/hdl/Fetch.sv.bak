`timescale 1ns / 1ps

module Fetch #(parameter BITS = 32) (
	input logic [BITS-1:0] ALUSResultE, ResultW,
	input logic CLK,PCSrcW,BranchE,StallF,
	output logic [BITS-1:0] InstrF, PCPlus4F);

	logic [BITS-1:0] PC,PCF,MuxCon;
	
	RegPC RegPC(
		.pcIn(PC),
		.stall(StallF),
		.CLK(CLK),
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

	instructionMemory MemoriaInst(
		.a(PCF),
		.rd(InstrF));

	adder Sumador(
		.a(PCF),
		.b(32'd4),
		.PCPlus4F(PCPlus4F));

endmodule