// Generated from Smeil.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class SmeilLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, T__36=37, T__37=38, 
		T__38=39, T__39=40, T__40=41, T__41=42, T__42=43, T__43=44, TYPENAME=45, 
		IDENT=46, INTEGER=47, FLOATING=48, NUMBER=49, LETTER=50, HEXDIGIT=51, 
		OCTALDIGIT=52, STRINGCHAR=53, WHITESPACE=54;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
		"T__9", "T__10", "T__11", "T__12", "T__13", "T__14", "T__15", "T__16", 
		"T__17", "T__18", "T__19", "T__20", "T__21", "T__22", "T__23", "T__24", 
		"T__25", "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", "T__32", 
		"T__33", "T__34", "T__35", "T__36", "T__37", "T__38", "T__39", "T__40", 
		"T__41", "T__42", "T__43", "TYPENAME", "IDENT", "INTEGER", "FLOATING", 
		"NUMBER", "LETTER", "HEXDIGIT", "OCTALDIGIT", "STRINGCHAR", "WHITESPACE"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'network'", "'('", "')'", "'{'", "'}'", "'proc'", "','", "'in'", 
		"'out'", "'const'", "'var'", "':'", "'='", "';'", "'range'", "'to'", "'exposed'", 
		"'bus'", "'instance'", "'of'", "'.'", "'trace'", "'\"'", "'{}'", "'+'", 
		"'-'", "'*'", "'/'", "'%'", "'=='", "'!='", "'<<'", "'>>'", "'<'", "'>'", 
		"'>='", "'<='", "'&'", "'|'", "'^'", "'&&'", "'||'", "'!'", "'~'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, null, "TYPENAME", "IDENT", 
		"INTEGER", "FLOATING", "NUMBER", "LETTER", "HEXDIGIT", "OCTALDIGIT", "STRINGCHAR", 
		"WHITESPACE"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public SmeilLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Smeil.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\28\u0144\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3"+
		"\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3"+
		"\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3"+
		"\16\3\16\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3"+
		"\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3"+
		"\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\27\3"+
		"\27\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3"+
		"\35\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#"+
		"\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3"+
		"-\3-\3.\3.\3.\3.\5.\u0100\n.\3/\3/\3/\3/\7/\u0106\n/\f/\16/\u0109\13/"+
		"\3\60\6\60\u010c\n\60\r\60\16\60\u010d\3\60\3\60\3\60\3\60\6\60\u0114"+
		"\n\60\r\60\16\60\u0115\3\60\3\60\3\60\3\60\6\60\u011c\n\60\r\60\16\60"+
		"\u011d\5\60\u0120\n\60\3\61\7\61\u0123\n\61\f\61\16\61\u0126\13\61\3\61"+
		"\3\61\6\61\u012a\n\61\r\61\16\61\u012b\3\62\3\62\3\63\5\63\u0131\n\63"+
		"\3\64\3\64\5\64\u0135\n\64\3\65\3\65\3\66\6\66\u013a\n\66\r\66\16\66\u013b"+
		"\3\67\6\67\u013f\n\67\r\67\16\67\u0140\3\67\3\67\2\28\3\3\5\4\7\5\t\6"+
		"\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24"+
		"\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K"+
		"\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8\3\2\b\4\2//aa\3\2"+
		"\62;\4\2C\\c|\4\2CHch\3\2\62:\5\2\13\f\17\17\"\"\2\u0151\2\3\3\2\2\2\2"+
		"\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2"+
		"\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2"+
		"\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2"+
		"\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2"+
		"\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2"+
		"\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2"+
		"K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3"+
		"\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2"+
		"\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\3o\3\2\2\2\5"+
		"w\3\2\2\2\7y\3\2\2\2\t{\3\2\2\2\13}\3\2\2\2\r\177\3\2\2\2\17\u0084\3\2"+
		"\2\2\21\u0086\3\2\2\2\23\u0089\3\2\2\2\25\u008d\3\2\2\2\27\u0093\3\2\2"+
		"\2\31\u0097\3\2\2\2\33\u0099\3\2\2\2\35\u009b\3\2\2\2\37\u009d\3\2\2\2"+
		"!\u00a3\3\2\2\2#\u00a6\3\2\2\2%\u00ae\3\2\2\2\'\u00b2\3\2\2\2)\u00bb\3"+
		"\2\2\2+\u00be\3\2\2\2-\u00c0\3\2\2\2/\u00c6\3\2\2\2\61\u00c8\3\2\2\2\63"+
		"\u00cb\3\2\2\2\65\u00cd\3\2\2\2\67\u00cf\3\2\2\29\u00d1\3\2\2\2;\u00d3"+
		"\3\2\2\2=\u00d5\3\2\2\2?\u00d8\3\2\2\2A\u00db\3\2\2\2C\u00de\3\2\2\2E"+
		"\u00e1\3\2\2\2G\u00e3\3\2\2\2I\u00e5\3\2\2\2K\u00e8\3\2\2\2M\u00eb\3\2"+
		"\2\2O\u00ed\3\2\2\2Q\u00ef\3\2\2\2S\u00f1\3\2\2\2U\u00f4\3\2\2\2W\u00f7"+
		"\3\2\2\2Y\u00f9\3\2\2\2[\u00ff\3\2\2\2]\u0101\3\2\2\2_\u011f\3\2\2\2a"+
		"\u0124\3\2\2\2c\u012d\3\2\2\2e\u0130\3\2\2\2g\u0134\3\2\2\2i\u0136\3\2"+
		"\2\2k\u0139\3\2\2\2m\u013e\3\2\2\2op\7p\2\2pq\7g\2\2qr\7v\2\2rs\7y\2\2"+
		"st\7q\2\2tu\7t\2\2uv\7m\2\2v\4\3\2\2\2wx\7*\2\2x\6\3\2\2\2yz\7+\2\2z\b"+
		"\3\2\2\2{|\7}\2\2|\n\3\2\2\2}~\7\177\2\2~\f\3\2\2\2\177\u0080\7r\2\2\u0080"+
		"\u0081\7t\2\2\u0081\u0082\7q\2\2\u0082\u0083\7e\2\2\u0083\16\3\2\2\2\u0084"+
		"\u0085\7.\2\2\u0085\20\3\2\2\2\u0086\u0087\7k\2\2\u0087\u0088\7p\2\2\u0088"+
		"\22\3\2\2\2\u0089\u008a\7q\2\2\u008a\u008b\7w\2\2\u008b\u008c\7v\2\2\u008c"+
		"\24\3\2\2\2\u008d\u008e\7e\2\2\u008e\u008f\7q\2\2\u008f\u0090\7p\2\2\u0090"+
		"\u0091\7u\2\2\u0091\u0092\7v\2\2\u0092\26\3\2\2\2\u0093\u0094\7x\2\2\u0094"+
		"\u0095\7c\2\2\u0095\u0096\7t\2\2\u0096\30\3\2\2\2\u0097\u0098\7<\2\2\u0098"+
		"\32\3\2\2\2\u0099\u009a\7?\2\2\u009a\34\3\2\2\2\u009b\u009c\7=\2\2\u009c"+
		"\36\3\2\2\2\u009d\u009e\7t\2\2\u009e\u009f\7c\2\2\u009f\u00a0\7p\2\2\u00a0"+
		"\u00a1\7i\2\2\u00a1\u00a2\7g\2\2\u00a2 \3\2\2\2\u00a3\u00a4\7v\2\2\u00a4"+
		"\u00a5\7q\2\2\u00a5\"\3\2\2\2\u00a6\u00a7\7g\2\2\u00a7\u00a8\7z\2\2\u00a8"+
		"\u00a9\7r\2\2\u00a9\u00aa\7q\2\2\u00aa\u00ab\7u\2\2\u00ab\u00ac\7g\2\2"+
		"\u00ac\u00ad\7f\2\2\u00ad$\3\2\2\2\u00ae\u00af\7d\2\2\u00af\u00b0\7w\2"+
		"\2\u00b0\u00b1\7u\2\2\u00b1&\3\2\2\2\u00b2\u00b3\7k\2\2\u00b3\u00b4\7"+
		"p\2\2\u00b4\u00b5\7u\2\2\u00b5\u00b6\7v\2\2\u00b6\u00b7\7c\2\2\u00b7\u00b8"+
		"\7p\2\2\u00b8\u00b9\7e\2\2\u00b9\u00ba\7g\2\2\u00ba(\3\2\2\2\u00bb\u00bc"+
		"\7q\2\2\u00bc\u00bd\7h\2\2\u00bd*\3\2\2\2\u00be\u00bf\7\60\2\2\u00bf,"+
		"\3\2\2\2\u00c0\u00c1\7v\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3\7c\2\2\u00c3"+
		"\u00c4\7e\2\2\u00c4\u00c5\7g\2\2\u00c5.\3\2\2\2\u00c6\u00c7\7$\2\2\u00c7"+
		"\60\3\2\2\2\u00c8\u00c9\7}\2\2\u00c9\u00ca\7\177\2\2\u00ca\62\3\2\2\2"+
		"\u00cb\u00cc\7-\2\2\u00cc\64\3\2\2\2\u00cd\u00ce\7/\2\2\u00ce\66\3\2\2"+
		"\2\u00cf\u00d0\7,\2\2\u00d08\3\2\2\2\u00d1\u00d2\7\61\2\2\u00d2:\3\2\2"+
		"\2\u00d3\u00d4\7\'\2\2\u00d4<\3\2\2\2\u00d5\u00d6\7?\2\2\u00d6\u00d7\7"+
		"?\2\2\u00d7>\3\2\2\2\u00d8\u00d9\7#\2\2\u00d9\u00da\7?\2\2\u00da@\3\2"+
		"\2\2\u00db\u00dc\7>\2\2\u00dc\u00dd\7>\2\2\u00ddB\3\2\2\2\u00de\u00df"+
		"\7@\2\2\u00df\u00e0\7@\2\2\u00e0D\3\2\2\2\u00e1\u00e2\7>\2\2\u00e2F\3"+
		"\2\2\2\u00e3\u00e4\7@\2\2\u00e4H\3\2\2\2\u00e5\u00e6\7@\2\2\u00e6\u00e7"+
		"\7?\2\2\u00e7J\3\2\2\2\u00e8\u00e9\7>\2\2\u00e9\u00ea\7?\2\2\u00eaL\3"+
		"\2\2\2\u00eb\u00ec\7(\2\2\u00ecN\3\2\2\2\u00ed\u00ee\7~\2\2\u00eeP\3\2"+
		"\2\2\u00ef\u00f0\7`\2\2\u00f0R\3\2\2\2\u00f1\u00f2\7(\2\2\u00f2\u00f3"+
		"\7(\2\2\u00f3T\3\2\2\2\u00f4\u00f5\7~\2\2\u00f5\u00f6\7~\2\2\u00f6V\3"+
		"\2\2\2\u00f7\u00f8\7#\2\2\u00f8X\3\2\2\2\u00f9\u00fa\7\u0080\2\2\u00fa"+
		"Z\3\2\2\2\u00fb\u00fc\7k\2\2\u00fc\u0100\5_\60\2\u00fd\u00fe\7w\2\2\u00fe"+
		"\u0100\5_\60\2\u00ff\u00fb\3\2\2\2\u00ff\u00fd\3\2\2\2\u0100\\\3\2\2\2"+
		"\u0101\u0107\5e\63\2\u0102\u0106\5e\63\2\u0103\u0106\5c\62\2\u0104\u0106"+
		"\t\2\2\2\u0105\u0102\3\2\2\2\u0105\u0103\3\2\2\2\u0105\u0104\3\2\2\2\u0106"+
		"\u0109\3\2\2\2\u0107\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u0108^\3\2\2\2"+
		"\u0109\u0107\3\2\2\2\u010a\u010c\5c\62\2\u010b\u010a\3\2\2\2\u010c\u010d"+
		"\3\2\2\2\u010d\u010b\3\2\2\2\u010d\u010e\3\2\2\2\u010e\u0120\3\2\2\2\u010f"+
		"\u0110\7\62\2\2\u0110\u0111\7z\2\2\u0111\u0113\3\2\2\2\u0112\u0114\5g"+
		"\64\2\u0113\u0112\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0113\3\2\2\2\u0115"+
		"\u0116\3\2\2\2\u0116\u0120\3\2\2\2\u0117\u0118\7\62\2\2\u0118\u0119\7"+
		"q\2\2\u0119\u011b\3\2\2\2\u011a\u011c\5i\65\2\u011b\u011a\3\2\2\2\u011c"+
		"\u011d\3\2\2\2\u011d\u011b\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u0120\3\2"+
		"\2\2\u011f\u010b\3\2\2\2\u011f\u010f\3\2\2\2\u011f\u0117\3\2\2\2\u0120"+
		"`\3\2\2\2\u0121\u0123\5c\62\2\u0122\u0121\3\2\2\2\u0123\u0126\3\2\2\2"+
		"\u0124\u0122\3\2\2\2\u0124\u0125\3\2\2\2\u0125\u0127\3\2\2\2\u0126\u0124"+
		"\3\2\2\2\u0127\u0129\7\60\2\2\u0128\u012a\5c\62\2\u0129\u0128\3\2\2\2"+
		"\u012a\u012b\3\2\2\2\u012b\u0129\3\2\2\2\u012b\u012c\3\2\2\2\u012cb\3"+
		"\2\2\2\u012d\u012e\t\3\2\2\u012ed\3\2\2\2\u012f\u0131\t\4\2\2\u0130\u012f"+
		"\3\2\2\2\u0131f\3\2\2\2\u0132\u0135\5c\62\2\u0133\u0135\t\5\2\2\u0134"+
		"\u0132\3\2\2\2\u0134\u0133\3\2\2\2\u0135h\3\2\2\2\u0136\u0137\t\6\2\2"+
		"\u0137j\3\2\2\2\u0138\u013a\5e\63\2\u0139\u0138\3\2\2\2\u013a\u013b\3"+
		"\2\2\2\u013b\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013cl\3\2\2\2\u013d\u013f"+
		"\t\7\2\2\u013e\u013d\3\2\2\2\u013f\u0140\3\2\2\2\u0140\u013e\3\2\2\2\u0140"+
		"\u0141\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0143\b\67\2\2\u0143n\3\2\2\2"+
		"\20\2\u00ff\u0105\u0107\u010d\u0115\u011d\u011f\u0124\u012b\u0130\u0134"+
		"\u013b\u0140\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}