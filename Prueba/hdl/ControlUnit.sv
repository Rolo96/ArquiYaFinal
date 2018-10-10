`timescale 1ns / 1ps

module ControlUnit(
	input logic [1:0] Op,//tipo de instruccion
	input logic [5:0] Funct, // I-OpCode-S / intrucc[25:20]
	input logic [3:0] Rd, //destino
	output logic [1:0] FlagW, //usar banderas condicionales
	output logic PCS, RegW, MemW, //escribir pc/escribir en reg/ escribir en mem
	output logic MemtoReg, ALUSrc,Branch, //memtoReg=senal para mux de wb / aluSrc: senal para mux de imm en exe
	output logic [1:0] ImmSrc, RegSrc, //tipo de ext de signo para imm / senal para muxes de regs en deco
	output logic [3:0] ALUControl,
	output logic NoWrite //si la instruccion es un cmp
	);
	
	logic [9:0] controls;
	logic BranchTemp, ALUOp;

// Main Decoder
	always_comb
		case(Op)
			2'b00: 
				if (Funct[5]) controls = 10'b0000101001; // Data-processing immediate
				else controls = 10'b0000001001; // Data-processing register
			
			2'b01: 
				if (Funct[0]) controls = 10'b0001111000;// LDR
				else controls = 10'b1001110100;// STR
				
			2'b10: 
				controls = 10'b0110100010;// B
				
			2'b11:
				controls = 10'b0011101001;

			default: controls = 10'bx;
		endcase
		
	assign {RegSrc, ImmSrc, ALUSrc, MemtoReg, RegW, MemW, BranchTemp, ALUOp} = controls;
	
	always_comb
		if (ALUOp) begin // si se usa la alu
			case(Funct[4:1]) //cual instruccion de dataproccessing
				4'b0000: ALUControl = 4'b0000; // ADD
				4'b0001: ALUControl = 4'b0001; // SUB
				4'b0010: ALUControl = 4'b0010; // MUL
				4'b0011: ALUControl = 4'b1000; // MOV
				4'b1000: ALUControl = 4'b0100; // AND
				4'b1001: ALUControl = 4'b0101; // ORR
				4'b1010: ALUControl = 4'b0110; // PRD
				4'b1011: ALUControl = 4'b0011; // BRD
				4'b0100: ALUControl = 4'b0001; // CMP
				4'b1100: ALUControl = 4'b1100; // STP
				4'b1101: ALUControl = 4'b1101; // CME
				4'b1111: ALUControl = 4'b1000; // ADR
				default: ALUControl = 4'bx;
			endcase
			// update flags if S bit is set (C & V only for arith)
			FlagW[1] = Funct[0];
			FlagW[0] = Funct[0] & (ALUControl == 4'b0000 | ALUControl == 4'b0001);
		end else begin
			ALUControl = 4'b0000; // add para instruccion no-dataproccessing
			FlagW = 2'b00; //no actualizar banderas
		end
	// PC Logic
	assign PCS = ((Rd == 4'b1111) & RegW) | Branch;
	assign NoWrite = (Funct[4:1]==4'b0100|Funct[4:1]==4'b1101) & ALUOp;
	assign Branch = BranchTemp;
endmodule
