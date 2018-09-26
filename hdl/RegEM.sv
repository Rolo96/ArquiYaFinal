`timescale 1ns / 1ps

module RegEM #(parameter BITS = 32) (
	input logic [BITS-1:0] ALUResultE, WriteDataE, 
	input logic PCSrcE,RegWriteE,MemtoRegE,MemWriteE,CLK,
	input logic [3:0] WA3E,

	output logic [BITS-1:0] ALUResultM, WriteDataM, 
	output logic PCSrcM,RegWriteM,MemtoRegM,MemWriteM,
	output logic [3:0] WA3M);
	
	always_ff@(posedge CLK)
	begin
		WA3M = WA3E;
		PCSrcM = PCSrcE;
		RegWriteM = RegWriteE;
		MemtoRegM = MemtoRegE;
		MemWriteM = MemWriteE;
		ALUResultM = ALUResultE;
		WriteDataM = WriteDataE;
	end
endmodule