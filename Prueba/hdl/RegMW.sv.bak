`timescale 1ns / 1ps

module RegMW #(parameter BITS = 32) (
	input logic [BITS-1:0] ALUOutM, ReadDataM, 
	input logic PCSrcM,RegWriteM,MemtoRegM,CLK,
	input logic [3:0] WA3M,

	output logic [BITS-1:0] ALUOutW, ReadDataW, 
	output logic PCSrcW,RegWriteW,MemtoRegW,
	output logic [3:0] WA3W);
	
	always_ff@(posedge CLK)
	begin
		WA3W = WA3M;
		PCSrcW = PCSrcM;
		RegWriteW = RegWriteM;
		MemtoRegW = MemtoRegM;
		ALUOutW = ALUOutM;
		ReadDataW = ReadDataM;
	end
endmodule