`timescale 1ns / 1ps

module ALU #(parameter BITS = 32) (
	input logic [BITS-1:0] SrcAE,SrcBE,
	input logic [2:0] ALUControlE, 
	output logic [3:0] ALUFlags,
	output logic [BITS-1:0] ALUResultE);

	logic [BITS-1:0] ALUResultTemp;
	logic cin, cout;
	logic [BITS-1:0] negative;
	
	always_comb
	begin 
	cin='b0;
	cout='b0;
	negative=32'b0;
	ALUResultTemp=32'b0;
		case(ALUControlE)
			3'b000 : //ADD
			begin 
				{cin, ALUResultTemp[BITS-2:0]} = SrcAE[BITS-2:0] + SrcBE[BITS-2:0]; 
				{cout, ALUResultTemp[BITS-1]} = cin + SrcAE[BITS-1] + SrcBE[BITS-1];
			end
			
			3'b001 : //SUB
			begin 
				negative = -SrcBE;
				{cin, ALUResultTemp[BITS-2:0]} = SrcAE[BITS-2:0] + negative[BITS-2:0]; 
				{cout, ALUResultTemp[BITS-1]} = cin + SrcAE[BITS-1] + negative[BITS-1];
			end
			
			3'b010 :  //MUL 
			begin 
				ALUResultTemp = SrcAE * SrcBE;
			end
			
			3'b100 :  //AND 
			begin 
				ALUResultTemp = SrcAE & SrcBE;
			end
			
			3'b101 :  //OR 
			begin 
				ALUResultTemp = SrcAE | SrcBE; 
			end
			
			3'b011 : //Acum 
			begin 
				ALUResultTemp = SrcAE + {24'b0, SrcBE[7:0]}; 
			end
			
			3'b110 : //Prom
			begin 
				ALUResultTemp = SrcAE[7:0]+SrcAE[15:8]+SrcAE[23:16];
				ALUResultTemp += (ALUResultTemp+2) >> 2;
				ALUResultTemp += (ALUResultTemp+8) >> 4;
				ALUResultTemp += (ALUResultTemp+128) >> 8;
				ALUResultTemp >>= 2;
			end
			
			3'b111 : //NOT Assigned 
			begin 
				ALUResultTemp = SrcAE | SrcBE; 
			end
			
			default: 
			begin 
				ALUResultTemp = 32'd0;
			end
		endcase
	end
	assign ALUResultE = ALUResultTemp;
	assign ALUFlags[1]  = cout;
	assign ALUFlags[0] = cin^cout;
	assign ALUFlags[3] = ALUResultE[BITS-1]; 	
	assign ALUFlags[2] = (ALUResultE == 0);
endmodule