`timescale 1ns / 1ps

module TopModule #(parameter BITS = 32) (
	input logic CLK);


	logic [BITS-1:0] ALUSResultE, ResultW;
	logic PCSrcW,BranchE,StallF;
	logic [BITS-1:0] InstrF, PCPlus4F;

	logic [BITS-1:0] InstrD, PCPlus8D;
	logic [3:0] WA3W;
	logic [BITS-1:0] RD1D, RD2D,ExtImmD, RD1E, RD2E,ExtImmE;
	logic PCSrcD,RegWriteD,MemtoRegD,MemWriteD,BranchD,ALUSrcD,NoWriteD;
	logic [1:0] FlagWriteD;
	logic [2:0] ALUControlD;
	logic [3:0] FlagsD, CondD,WA3D, FlagsE;

	logic RegWriteM, RegWriteW, MemToRegE, BranchTakenE, PCSrcE, PCSrcM, Reset;
	logic [3:0] RA1D, RA2D, RA1E, RA2E, WA3M, WA3E;
	logic [1:0] FowardAE, FowardBE;
	logic StallD, FlushD, FlushE;

	logic [BITS-1:0] ALUOutM, ReadDataM;
	logic MemtoRegM;
	logic [BITS-1:0] ALUOutW, ReadDataW;
	logic MemtoRegW;

	logic [BITS-1:0] ALUResultE, WriteDataE;
	logic MemWriteE;

	logic [BITS-1:0] ALUResultM, WriteDataM;
	logic MemWriteM;

	logic RegWriteE,ALUSrcE,FlagWriteE,NoWriteE;
	logic [2:0] ALUControlE;
	logic [3:0] CondE;

	logic PCSrcEOut,RegWriteEOut,BranchEOut,MemWriteEOut;


	
	
	Fetch Fetch(
		.ALUSResultE(ALUSResultE),
		.ResultW(ResultW),
		.CLK(CLK),
		.PCSrcW(PCSrcW),
		.BranchE(BranchEOut),
		.StallF(StallF),
		.InstrF(InstrF),
		.PCPlus4F(PCPlus4F)
	);	

	Deco Deco(
		.InstrD(InstrD),
		.PCPlus8D(PCPlus4F),
		.ResultW(ResultW),
		.CLK(CLK),
		.RegWriteW(RegWriteW),
		.WA3W(WA3W),
		.RD1D(RD1D),
		.RD2D(RD2D),
		.ExtImmD(ExtImmD),
		.PCSrcD(PCSrcD),
		.RegWriteD(RegWriteD),
		.MemtoRegD(MemtoRegD),
		.MemWriteD(MemWriteD),
		.BranchD(BranchD),
		.ALUSrcD(ALUSrcD),
		.NoWriteD(NoWriteD),
		.FlagWriteD(FlagWriteD),
		.ALUControlD(ALUControlD),
		.CondD(CondD),
		.WA3D(WA3D),
		.RA1D(RA1D),
		.RA2D(RA2D)
	);

	HazardUnit Hazard(
		.RegWriteM(RegWriteM),
		.RegWriteW(RegWriteW),
		.MemToRegE(MemToRegE),
		.BranchTakenE(BranchEOut),
		.PCSrcD(PCSrcD),
		.PCSrcE(PCSrcE),
		.PCSrcM(PCSrcM),
		.PCSrcW(PCSrcW),
		.Reset(CLK),
		.RA1D(RA1D),
		.RA2D(RA2D),
		.RA1E(RA1E),
		.RA2E(RA2E),
		.WA3M(WA3M),
		.WA3W(WA3W),
		.WA3E(WA3E),
		.FowardAE(FowardAE),
		.FowardBE(FowardBE),
		.StallF(StallF),
		.StallD(StallD),
		.FlushD(FlushD),
		.FlushE(FlushE)
	);

	Mux2 mux2WB(
		.d0(ALUOutW),
		.d1(ReadDataW),
		.s(MemtoRegW),
		.y(ResultW));

	DataMemory MemoriaDatos(
		.CLK(CLK),
		.WE(MemToRegE),
		.A(ALUOutM),
		.WD(WriteDataM),
		.RD(ReadDataM)
	);

	regFD RegFD(
		.CLK(CLK),
		.StallD(StallD),
		.CLR(FlushD),
		.InstrF(InstrF),
		.InstrD(InstrD)
	);

	RegDE RegDE(
		.RD1D(RD1D),
		.RD2D(RD2D),
		.ExtImmD(ExtImmD),
		.PCSrcD(PCSrcD),
		.RegWriteD(RegWriteD),
		.MemtoRegD(MemtoRegD),
		.MemWriteD(MemWriteD),
		.BranchD(BranchD),
		.ALUSrcD(ALUSrcD),
		.CLR(FlushE),
		.CLK(CLK),
		.NoWriteD(NoWriteD),
		.FlagWriteD(FlagWriteD),
		.ALUControlD(ALUControlD),
		.FlagsD(FlagsD),
		.CondD(CondD),
		.WA3D(WA3D),
		.RA1D(RA1D),
		.RA2D(RA2D),
		.PCSrcE(PCSrcE),
		.RegWriteE(RegWriteE),
		.MemtoRegE(MemToRegE),
		.MemWriteE(MemWriteE),
		.BranchE(BranchE),
		.ALUSrcE(ALUSrcE),
		.NoWriteE(NoWriteE),
		.FlagWriteE(FlagWriteE),
		.ALUControlE(ALUControlE),
		.FlagsE(FlagsE),
		.CondE(CondE),
		.WA3E(WA3E),
		.RA1E(RA1E),
		.RA2E(RA2E), 
		.RD1E(RD1E),
		.RD2E(RD2E),
		.ExtImmE(ExtImmE)
	);

	RegEM RegEM(
		.ALUResultE(ALUResultE),
		.WriteDataE(WriteDataE),
		.PCSrcE(PCSrcEOut),
		.RegWriteE(RegWriteEOut),
		.MemtoRegE(MemToRegE),
		.MemWriteE(MemWriteEOut),
		.CLK(CLK),
		.WA3E(WA3E),
		.ALUResultM(ALUOutM),
		.WriteDataM(WriteDataM),
		.PCSrcM(PCSrcM),
		.RegWriteM(RegWriteM),
		.MemtoRegM(RegWriteM),
		.MemWriteM(MemWriteM),
		.WA3M(WA3M)
	);

	RegMW RegMW(
		.ALUOutM(ALUOutM),
		.ReadDataM(ReadDataM),
		.PCSrcM(PCSrcM),
		.RegWriteM(RegWriteM),
		.MemtoRegM(MemtoRegM),
		.CLK(CLK),
		.WA3M(WA3M),
		.ALUOutW(ALUOutW),
		.ReadDataW(ReadDataW),
		.PCSrcW(PCSrcW),
		.RegWriteW(RegWriteW),
		.MemtoRegW(MemtoRegW),
		.WA3W(WA3W)
	);

	Execute Execute(
		.CLK(CLK),
		.RESET(CLK),
		.PCSrcE(PCSrcE),
		.NoWrite(NoWriteE),
		.RegWriteE(RegWriteE),
		.MemWriteE(MemWriteE),
		.BranchE(BranchE),
		.ALUSrcE(ALUSrcE),
		.FlagsWriteE(FlagWriteE),
		.ForwardAE(FowardAE),
		.ForwardBE(FowardBE),
		.ALUControlE(ALUControlE),
		.CondE(CondE),
		.FlagsE(FlagsE),
		.RD1E(RD1E),
		.RD2E(RD2E),
		.ExtImmE(ExtImmE),
		.ResultW(ResultW),
		.ALUResultM(ALUOutM),
		.ALUFlagsEOut(FlagsD),
		.PCSrcEOut(PCSrcEOut),
		.RegWriteEOut(RegWriteEOut),
		.BranchEOut(BranchEOut),
		.MemWriteEOut(MemWriteEOut),
		.ALUResultE(ALUResultE),
		.WriteDataE(WriteDataE)
	);

endmodule