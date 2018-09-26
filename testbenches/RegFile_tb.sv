`timescale 1ns / 1ps

module RegFile_tb;
	// Inputs
	bit clk;
	bit we3;
	logic [3:0] a1;
	logic [3:0] a2;
	logic [3:0] wa3;
	logic [31:0] wd3;
	logic [31:0] r15;
	
	//Outputs
	logic [31:0] rd1;
	logic [31:0] rd2;

	//Instancia del Device Under Test (DUT)
	RegFile DUT( 
		.clk( clk ),
		.we3( we3 ),
		.a1( a1 ),
		.a2( a2 ),
		.wa3( wa3 ),
		.wd3( wd3 ),
		.r15( r15 ),
		.rd1( rd1 ),
		.rd2( rd2 ) );

	//Inicializa clock
	initial begin
		clk = 1'b1;
		forever begin
			#5;
			clk = ~clk;
		end
	end

	initial begin
		// Inicializa Inputs
		a1 = 4'bxxxx;
		a2 = 4'bxxxx;
		wa3 = 4'bxxxx;
		wd3 = 4'bxxxx;
		r15 = 4'bxxxx;
		
		//Valores iniciales para guardar en registros
		wa3 = 4'b0000;
		we3 = 1'b1;
		wd3 = 32'd4;
		
		//loop para guardar un dato diferente en diferente direccion de memoria
		for( int i=0; i<16; i++ ) 
			begin
				#10;
				wa3 = wa3 + 1'b1;    
				wd3 = wd3 + 32'd4;
			end

		//se cierran los imputs
		we3 = 1'b0;
		wa3 = 4'bxxxx;
		wd3 = 32'bx;
		
		#10;
		
		//se inicializan las direcciones de salidas
		a1 = 4'b0000;
		a2 = 4'b0001;
		r15 = 32'b11001101001110011110000011111010;
		//loop para leer los registros 
		for( int j=0; j<8; j++ ) 
			begin
				#10;
				a1 = a1 + 2'b10;
				a2 = a2 + 2'b10;
			end
		$stop;
	end
endmodule
