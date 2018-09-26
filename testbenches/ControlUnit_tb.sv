`timescale 1ns / 1ps

module ControlUnit_tb();
	logic [31:0] instruction;
	logic [1:0] Op;
	logic [5:0] Funct; // I-OpCode-S / intrucc[25:20]
	logic [3:0] Rd; //reg destino
	
	logic [1:0] FlagW;
	bit PCS;
	bit RegW;
	bit MemW;
	bit MemtoReg;
	bit ALUSrc;
	bit NoWrite;
	logic [1:0] ImmSrc;
	logic [1:0] RegSrc;
	logic [2:0] ALUControl;
	
	ControlUnit DUT(
		.Op(Op),
		.Funct(Funct),
		.Rd(Rd),
		.FlagW(FlagW),
		.PCS(PCS),
		.RegW(RegW),
		.MemW(MemW),
		.MemtoReg(MemtoReg),
		.ALUSrc(ALUSrc),
		.ImmSrc(ImmSrc),
		.RegSrc(RegSrc),
		.ALUControl(ALUControl),
		.NoWrite(NoWrite)
	);
	
	initial begin
		//data proccessing registro (ADD) no activa S
		instruction = 32'b00000000000010101011000000001101; 
		Op = instruction[27:26];
		Funct = instruction[25:20];
		Rd = instruction[15:12];
		#5;
		
		//data proccessing inmediato (SUB) activa S
		instruction = 32'b00000010001110101011000011111111;
		Op = instruction[27:26];
		Funct = instruction[25:20];
		Rd = instruction[15:12];
		#5;
		
		//load inmediato
		instruction = 32'b00000110000110101011111110001111;
		Op = instruction[27:26];
		Funct = instruction[25:20];
		Rd = instruction[15:12];
		#5;
		
		//store
		instruction = 32'b00000100000010101011000000000010;
		Op = instruction[27:26];
		Funct = instruction[25:20];
		Rd = instruction[15:12];
		#5;

		//branch
		instruction = 32'b00001000100110011111101110111000; 
		Op = instruction[27:26];
		Funct = instruction[25:20];
		Rd = instruction[15:12];		
		#5;

	end
endmodule
