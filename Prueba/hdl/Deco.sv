`timescale 1ns / 1ps

module Deco #(parameter BITS = 32) (
	input logic [BITS-1:0] InstrD, PCPlus8D, ResultW,
	input logic CLK,RegWriteW,RESET,
	input logic [3:0] WA3W,
	output logic [BITS-1:0] RD1D, RD2D,ExtImmD,
	output logic PCSrcD,RegWriteD,MemtoRegD,MemWriteD,BranchD,ALUSrcD,NoWriteD,
	output logic [1:0] FlagWriteD,
	output logic [3:0] ALUControlD,
	output logic [3:0] Rd,CondD,WA3D, RA1D, RA2D);

	logic [1:0] Op,ImmSrc;
	logic [5:0] Funct;
	logic [23:0] ExtIn;
	logic [1:0] RegSrcD;
	logic [3:0] DecoRA1D,DecoRA2D;
	
	Decoder Decoder(
		.InstrD(InstrD),
		.Op(Op),
		.Funct(Funct),
		.Rd(Rd),
		.CondD(CondD),
		.RA1D(DecoRA1D),
		.RA2D(DecoRA2D),
		.WA3D(WA3D),
		.ExtImmD(ExtIn));

	Mux2 #(.BITS(4)) mux2Entrada1(
		.d0(DecoRA1D),
		.d1(4'd15),
		.s(RegSrcD[0]),
		.y(RA1D));

	Mux2 #(.BITS(4)) mux2Entrada2(
		.d0(DecoRA2D),
		.d1(WA3D),
		.s(RegSrcD[1]),
		.y(RA2D));

	Extend extend(
		.InstrD(ExtIn),
		.ImmSrcD(ImmSrc),
		.ExtImm(ExtImmD));

	ControlUnit UnidadControl(
		.Op(Op),
		.Funct(Funct),
		.Rd(Rd),
		.FlagW(FlagWriteD),
		.PCS(PCSrcD),
		.RegW(RegWriteD),
		.MemW(MemWriteD),
		.MemtoReg(MemtoRegD),
		.Branch(BranchD),
		.ALUSrc(ALUSrcD),
		.ImmSrc(ImmSrc),
		.RegSrc(RegSrcD),
		.ALUControl(ALUControlD),
		.NoWrite(NoWriteD));

	RegFile Registros(
		.clk(CLK),
		.reset(RESET),
		.we3(RegWriteW),
		.a1(RA1D),
		.a2(RA2D),
		.wa3(WA3W),
		.wd3(ResultW),
		.r15(PCPlus8D),
		.rd1(RD1D),
		.rd2(RD2D)
	);

endmodule