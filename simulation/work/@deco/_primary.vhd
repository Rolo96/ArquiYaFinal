library verilog;
use verilog.vl_types.all;
entity Deco is
    generic(
        BITS            : integer := 32
    );
    port(
        InstrD          : in     vl_logic_vector;
        PCPlus8D        : in     vl_logic_vector;
        ResultW         : in     vl_logic_vector;
        CLK             : in     vl_logic;
        RegWriteW       : in     vl_logic;
        WA3W            : in     vl_logic_vector(3 downto 0);
        RD1D            : out    vl_logic_vector;
        RD2D            : out    vl_logic_vector;
        ExtImmD         : out    vl_logic_vector;
        PCSrcD          : out    vl_logic;
        RegWriteD       : out    vl_logic;
        MemtoRegD       : out    vl_logic;
        MemWriteD       : out    vl_logic;
        BranchD         : out    vl_logic;
        ALUSrcD         : out    vl_logic;
        NoWriteD        : out    vl_logic;
        FlagWriteD      : out    vl_logic_vector(1 downto 0);
        ALUControlD     : out    vl_logic_vector(2 downto 0);
        CondD           : out    vl_logic_vector(3 downto 0);
        WA3D            : out    vl_logic_vector(3 downto 0);
        RA1D            : out    vl_logic_vector(3 downto 0);
        RA2D            : out    vl_logic_vector(3 downto 0)
    );
    attribute mti_svvh_generic_type : integer;
    attribute mti_svvh_generic_type of BITS : constant is 1;
end Deco;
