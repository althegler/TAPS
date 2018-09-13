// Generated from Example.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class ExampleLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		IDENT=1, INTEGER=2, LETTER=3, NUMBER=4, WHITESPACE=5;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"IDENT", "INTEGER", "LETTER", "NUMBER", "WHITESPACE"
	};

	private static final String[] _LITERAL_NAMES = {
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "IDENT", "INTEGER", "LETTER", "NUMBER", "WHITESPACE"
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


	public ExampleLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Example.g4"; }

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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7\'\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2\3\2\7\2\22\n\2\f\2\16\2\25"+
		"\13\2\3\3\6\3\30\n\3\r\3\16\3\31\3\4\5\4\35\n\4\3\5\3\5\3\6\6\6\"\n\6"+
		"\r\6\16\6#\3\6\3\6\2\2\7\3\3\5\4\7\5\t\6\13\7\3\2\6\4\2//aa\4\2C\\c|\3"+
		"\2\62;\5\2\13\f\17\17\"\"\2+\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3"+
		"\2\2\2\2\13\3\2\2\2\3\r\3\2\2\2\5\27\3\2\2\2\7\34\3\2\2\2\t\36\3\2\2\2"+
		"\13!\3\2\2\2\r\23\5\7\4\2\16\22\5\7\4\2\17\22\5\t\5\2\20\22\t\2\2\2\21"+
		"\16\3\2\2\2\21\17\3\2\2\2\21\20\3\2\2\2\22\25\3\2\2\2\23\21\3\2\2\2\23"+
		"\24\3\2\2\2\24\4\3\2\2\2\25\23\3\2\2\2\26\30\5\t\5\2\27\26\3\2\2\2\30"+
		"\31\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2\32\6\3\2\2\2\33\35\t\3\2\2\34"+
		"\33\3\2\2\2\35\b\3\2\2\2\36\37\t\4\2\2\37\n\3\2\2\2 \"\t\5\2\2! \3\2\2"+
		"\2\"#\3\2\2\2#!\3\2\2\2#$\3\2\2\2$%\3\2\2\2%&\b\6\2\2&\f\3\2\2\2\b\2\21"+
		"\23\31\34#\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}