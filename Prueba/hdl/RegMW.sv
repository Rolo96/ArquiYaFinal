`timescale 1ns / 1ps

module RegMW #(parameter BITS = 32) (
	input logic [BITS-1:0] ALUOutM, ReadDataM, 
	input logic PCSrcM,RegWriteM,MemtoRegM,CLK,RESET,
	input logic [3:0] WA3M,

	output logic [BITS-1:0] ALUOutW, ReadDataW, 
	output logic PCSrcW,RegWriteW,MemtoRegW,
	output logic [3:0] WA3W);
	
	always_ff@(negedge CLK)
	begin
		if(~RESET)begin
		WA3W = WA3M;
		PCSrcW = PCSrcM;
		RegWriteW = RegWriteM;
		MemtoRegW = MemtoRegM;
		ALUOutW = ALUOutM;
		ReadDataW = ReadDataM;
		end
		else begin
		WA3W = WA3M;
		PCSrcW = 1'b0;
		RegWriteW = 1'b0;
		MemtoRegW = 1'b0;
		ALUOutW = ALUOutM;
		ReadDataW = ReadDataM;
		end
	end
endmodule