`timescale 1ns / 1ps

module RegDE #(parameter BITS = 32) (
	input logic [BITS-1:0] RD1D, RD2D,ExtImmD,
	input logic PCSrcD,RegWriteD,MemtoRegD,MemWriteD,BranchD,ALUSrcD,CLR,CLK,NoWriteD,
	input logic [1:0] FlagWriteD,
	input logic [2:0] ALUControlD,
	input logic [3:0] FlagsD, CondD, WA3D, RA1D,RA2D,

	output logic [BITS-1:0] RD1E, RD2E,ExtImmE,
	output logic PCSrcE,RegWriteE,MemtoRegE,MemWriteE,BranchE,ALUSrcE,FlagWriteE,NoWriteE,
	output logic [2:0] ALUControlE,
	output logic [3:0] FlagsE, CondE, WA3E,RA1E,RA2E);
	
	always_ff@(posedge CLK)
	begin 
		if (CLR) 
		begin
			CondE = 4'd0;
			WA3E = 4'd0;	
			PCSrcE = 1'd0;
			RegWriteE = 1'd0;
			MemtoRegE = 1'd0;
			MemWriteE = 1'd0;
			ALUControlE = 3'd0; 
			BranchE = 1'd0;
			ALUSrcE = 1'd0;
			FlagWriteE = 2'd0;
			FlagsE = 4'd0;
			RD1E = 32'd0;
			RD2E = 32'd0;
			ExtImmE = 32'd0;
			NoWriteE = 1'd0;
			RA1E = 4'd0;
			RA2E = 4'd0;
		end
		else
		begin
			CondE = CondD;
			WA3E = WA3D;
			PCSrcE = PCSrcD;
			RegWriteE = RegWriteD;
			MemtoRegE = MemtoRegD;
			MemWriteE = MemWriteD;
			ALUControlE = ALUControlD; 
			BranchE = BranchD;
			ALUSrcE = ALUSrcD;
			FlagWriteE = FlagWriteD;
			FlagsE = FlagsD;
			RD1E = RD1D;
			RD2E = RD2D;
			ExtImmE = ExtImmD;
			NoWriteE = 1'd0;
			RA1E = RA1D;
			RA2E = RA2D;
		end
	end
endmodule