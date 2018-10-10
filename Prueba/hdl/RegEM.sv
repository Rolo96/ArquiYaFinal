`timescale 1ns / 1ps

module RegEM(	
	input logic CLK,RESET,
	input logic PCSrcECond,
	input logic RegWriteECond,
	input logic MemtoRegECond,
	input logic MemWriteECond,
	input logic [31:0] ALUResultE,
	input logic [31:0] WriteDataE,
	input logic [3:0] WA3E,

	
	output logic PCSrcM,
	output logic RegWriteM,
	output logic MemtoRegM,
	output logic MemWriteM,
	output logic [31:0] ALUResultM,
	output logic [31:0] WriteDataM,
	output logic [3:0] WA3M
);	

	always_ff @(negedge CLK)begin
		if(~RESET)begin
			PCSrcM = PCSrcECond;
			RegWriteM = RegWriteECond;
			MemtoRegM = MemtoRegECond;
			MemWriteM = MemWriteECond;
			ALUResultM = ALUResultE;
			WriteDataM = WriteDataE;
			WA3M = WA3E;
		end
		else begin
			PCSrcM = 1'b0;
			RegWriteM = 1'b0;
			MemtoRegM = 1'b0;
			MemWriteM = 1'b0;
			ALUResultM = ALUResultE;
			WriteDataM = WriteDataE;
			WA3M = WA3E;
		end
	
	end	

endmodule