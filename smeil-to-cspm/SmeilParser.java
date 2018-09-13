// Generated from Smeil.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class SmeilParser extends Parser {
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
		IDENT=46, ALPHA=47, NUM=48, WHITESPACE=49;
	public static final int
		RULE_module = 0, RULE_entity = 1, RULE_network = 2, RULE_process = 3, 
		RULE_networkdecl = 4, RULE_declaration = 5, RULE_params = 6, RULE_param = 7, 
		RULE_direction = 8, RULE_vardecl = 9, RULE_range = 10, RULE_busdecl = 11, 
		RULE_bussignaldecls = 12, RULE_bussignaldecl = 13, RULE_instance = 14, 
		RULE_instancename = 15, RULE_statement = 16, RULE_formatstring = 17, RULE_formatstringpart = 18, 
		RULE_expression = 19, RULE_binop = 20, RULE_unop = 21, RULE_literal = 22, 
		RULE_name = 23;
	public static final String[] ruleNames = {
		"module", "entity", "network", "process", "networkdecl", "declaration", 
		"params", "param", "direction", "vardecl", "range", "busdecl", "bussignaldecls", 
		"bussignaldecl", "instance", "instancename", "statement", "formatstring", 
		"formatstringpart", "expression", "binop", "unop", "literal", "name"
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
		"ALPHA", "NUM", "WHITESPACE"
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

	@Override
	public String getGrammarFileName() { return "Smeil.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public SmeilParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class ModuleContext extends ParserRuleContext {
		public List<EntityContext> entity() {
			return getRuleContexts(EntityContext.class);
		}
		public EntityContext entity(int i) {
			return getRuleContext(EntityContext.class,i);
		}
		public ModuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_module; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).enterModule(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).exitModule(this);
		}
	}

	public final ModuleContext module() throws RecognitionException {
		ModuleContext _localctx = new ModuleContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_module);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			entity();
			setState(52);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__0 || _la==T__5) {
				{
				{
				setState(49);
				entity();
				}
				}
				setState(54);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EntityContext extends ParserRuleContext {
		public NetworkContext network() {
			return getRuleContext(NetworkContext.class,0);
		}
		public ProcessContext process() {
			return getRuleContext(ProcessContext.class,0);
		}
		public EntityContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entity; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).enterEntity(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).exitEntity(this);
		}
	}

	public final EntityContext entity() throws RecognitionException {
		EntityContext _localctx = new EntityContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_entity);
		try {
			setState(57);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				enterOuterAlt(_localctx, 1);
				{
				setState(55);
				network();
				}
				break;
			case T__5:
				enterOuterAlt(_localctx, 2);
				{
				setState(56);
				process();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NetworkContext extends ParserRuleContext {
		public TerminalNode IDENT() { return getToken(SmeilParser.IDENT, 0); }
		public NetworkdeclContext networkdecl() {
			return getRuleContext(NetworkdeclContext.class,0);
		}
		public ParamsContext params() {
			return getRuleContext(ParamsContext.class,0);
		}
		public NetworkContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_network; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).enterNetwork(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).exitNetwork(this);
		}
	}

	public final NetworkContext network() throws RecognitionException {
		NetworkContext _localctx = new NetworkContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_network);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			match(T__0);
			setState(60);
			match(IDENT);
			setState(61);
			match(T__1);
			setState(63);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__7) | (1L << T__8) | (1L << T__9))) != 0)) {
				{
				setState(62);
				params();
				}
			}

			setState(65);
			match(T__2);
			setState(66);
			match(T__3);
			setState(67);
			networkdecl();
			setState(68);
			match(T__4);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ProcessContext extends ParserRuleContext {
		public TerminalNode IDENT() { return getToken(SmeilParser.IDENT, 0); }
		public ParamsContext params() {
			return getRuleContext(ParamsContext.class,0);
		}
		public List<DeclarationContext> declaration() {
			return getRuleContexts(DeclarationContext.class);
		}
		public DeclarationContext declaration(int i) {
			return getRuleContext(DeclarationContext.class,i);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProcessContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_process; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).enterProcess(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).exitProcess(this);
		}
	}

	public final ProcessContext process() throws RecognitionException {
		ProcessContext _localctx = new ProcessContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_process);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(70);
			match(T__5);
			setState(71);
			match(IDENT);
			setState(72);
			match(T__1);
			setState(74);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__7) | (1L << T__8) | (1L << T__9))) != 0)) {
				{
				setState(73);
				params();
				}
			}

			setState(76);
			match(T__2);
			setState(80);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__10) | (1L << T__16) | (1L << T__17))) != 0)) {
				{
				{
				setState(77);
				declaration();
				}
				}
				setState(82);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(83);
			match(T__3);
			setState(87);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__21) | (1L << IDENT) | (1L << NUM))) != 0)) {
				{
				{
				setState(84);
				statement();
				}
				}
				setState(89);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(90);
			match(T__4);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NetworkdeclContext extends ParserRuleContext {
		public List<InstanceContext> instance() {
			return getRuleContexts(InstanceContext.class);
		}
		public InstanceContext instance(int i) {
			return getRuleContext(InstanceContext.class,i);
		}
		public NetworkdeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_networkdecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).enterNetworkdecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).exitNetworkdecl(this);
		}
	}

	public final NetworkdeclContext networkdecl() throws RecognitionException {
		NetworkdeclContext _localctx = new NetworkdeclContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_networkdecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(95);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__18) {
				{
				{
				setState(92);
				instance();
				}
				}
				setState(97);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclarationContext extends ParserRuleContext {
		public VardeclContext vardecl() {
			return getRuleContext(VardeclContext.class,0);
		}
		public BusdeclContext busdecl() {
			return getRuleContext(BusdeclContext.class,0);
		}
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).enterDeclaration(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).exitDeclaration(this);
		}
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_declaration);
		try {
			setState(100);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__10:
				enterOuterAlt(_localctx, 1);
				{
				setState(98);
				vardecl();
				}
				break;
			case T__16:
			case T__17:
				enterOuterAlt(_localctx, 2);
				{
				setState(99);
				busdecl();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParamsContext extends ParserRuleContext {
		public List<ParamContext> param() {
			return getRuleContexts(ParamContext.class);
		}
		public ParamContext param(int i) {
			return getRuleContext(ParamContext.class,i);
		}
		public ParamsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_params; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).enterParams(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).exitParams(this);
		}
	}

	public final ParamsContext params() throws RecognitionException {
		ParamsContext _localctx = new ParamsContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_params);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(102);
			param();
			setState(107);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__6) {
				{
				{
				setState(103);
				match(T__6);
				setState(104);
				param();
				}
				}
				setState(109);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParamContext extends ParserRuleContext {
		public DirectionContext direction() {
			return getRuleContext(DirectionContext.class,0);
		}
		public TerminalNode IDENT() { return getToken(SmeilParser.IDENT, 0); }
		public ParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).enterParam(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).exitParam(this);
		}
	}

	public final ParamContext param() throws RecognitionException {
		ParamContext _localctx = new ParamContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_param);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(110);
			direction();
			setState(111);
			match(IDENT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DirectionContext extends ParserRuleContext {
		public DirectionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_direction; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).enterDirection(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).exitDirection(this);
		}
	}

	public final DirectionContext direction() throws RecognitionException {
		DirectionContext _localctx = new DirectionContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_direction);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(113);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__7) | (1L << T__8) | (1L << T__9))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VardeclContext extends ParserRuleContext {
		public TerminalNode IDENT() { return getToken(SmeilParser.IDENT, 0); }
		public TerminalNode TYPENAME() { return getToken(SmeilParser.TYPENAME, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public RangeContext range() {
			return getRuleContext(RangeContext.class,0);
		}
		public VardeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vardecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).enterVardecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).exitVardecl(this);
		}
	}

	public final VardeclContext vardecl() throws RecognitionException {
		VardeclContext _localctx = new VardeclContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_vardecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(115);
			match(T__10);
			setState(116);
			match(IDENT);
			setState(117);
			match(T__11);
			setState(118);
			match(TYPENAME);
			setState(121);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__12) {
				{
				setState(119);
				match(T__12);
				setState(120);
				expression(0);
				}
			}

			setState(124);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__14) {
				{
				setState(123);
				range();
				}
			}

			setState(126);
			match(T__13);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class RangeContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public RangeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_range; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).enterRange(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).exitRange(this);
		}
	}

	public final RangeContext range() throws RecognitionException {
		RangeContext _localctx = new RangeContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_range);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			match(T__14);
			setState(129);
			expression(0);
			setState(130);
			match(T__15);
			setState(131);
			expression(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BusdeclContext extends ParserRuleContext {
		public TerminalNode IDENT() { return getToken(SmeilParser.IDENT, 0); }
		public BussignaldeclsContext bussignaldecls() {
			return getRuleContext(BussignaldeclsContext.class,0);
		}
		public BusdeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_busdecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).enterBusdecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).exitBusdecl(this);
		}
	}

	public final BusdeclContext busdecl() throws RecognitionException {
		BusdeclContext _localctx = new BusdeclContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_busdecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(134);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__16) {
				{
				setState(133);
				match(T__16);
				}
			}

			setState(136);
			match(T__17);
			setState(137);
			match(IDENT);
			setState(138);
			match(T__3);
			setState(139);
			bussignaldecls();
			setState(140);
			match(T__4);
			setState(141);
			match(T__13);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BussignaldeclsContext extends ParserRuleContext {
		public List<BussignaldeclContext> bussignaldecl() {
			return getRuleContexts(BussignaldeclContext.class);
		}
		public BussignaldeclContext bussignaldecl(int i) {
			return getRuleContext(BussignaldeclContext.class,i);
		}
		public BussignaldeclsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bussignaldecls; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).enterBussignaldecls(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).exitBussignaldecls(this);
		}
	}

	public final BussignaldeclsContext bussignaldecls() throws RecognitionException {
		BussignaldeclsContext _localctx = new BussignaldeclsContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_bussignaldecls);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(143);
			bussignaldecl();
			setState(147);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==IDENT) {
				{
				{
				setState(144);
				bussignaldecl();
				}
				}
				setState(149);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BussignaldeclContext extends ParserRuleContext {
		public TerminalNode IDENT() { return getToken(SmeilParser.IDENT, 0); }
		public TerminalNode TYPENAME() { return getToken(SmeilParser.TYPENAME, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public RangeContext range() {
			return getRuleContext(RangeContext.class,0);
		}
		public BussignaldeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bussignaldecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).enterBussignaldecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).exitBussignaldecl(this);
		}
	}

	public final BussignaldeclContext bussignaldecl() throws RecognitionException {
		BussignaldeclContext _localctx = new BussignaldeclContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_bussignaldecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(150);
			match(IDENT);
			setState(151);
			match(T__11);
			setState(152);
			match(TYPENAME);
			setState(155);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__12) {
				{
				setState(153);
				match(T__12);
				setState(154);
				expression(0);
				}
			}

			setState(158);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__14) {
				{
				setState(157);
				range();
				}
			}

			setState(160);
			match(T__13);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InstanceContext extends ParserRuleContext {
		public InstancenameContext instancename() {
			return getRuleContext(InstancenameContext.class,0);
		}
		public TerminalNode IDENT() { return getToken(SmeilParser.IDENT, 0); }
		public List<NameContext> name() {
			return getRuleContexts(NameContext.class);
		}
		public NameContext name(int i) {
			return getRuleContext(NameContext.class,i);
		}
		public InstanceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instance; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).enterInstance(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).exitInstance(this);
		}
	}

	public final InstanceContext instance() throws RecognitionException {
		InstanceContext _localctx = new InstanceContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_instance);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(162);
			match(T__18);
			setState(163);
			instancename();
			setState(164);
			match(T__19);
			setState(165);
			match(IDENT);
			setState(166);
			match(T__1);
			setState(171);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==IDENT || _la==NUM) {
				{
				setState(167);
				name(0);
				setState(168);
				match(T__20);
				setState(169);
				name(0);
				}
			}

			setState(173);
			match(T__2);
			setState(174);
			match(T__13);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InstancenameContext extends ParserRuleContext {
		public TerminalNode IDENT() { return getToken(SmeilParser.IDENT, 0); }
		public InstancenameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_instancename; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).enterInstancename(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).exitInstancename(this);
		}
	}

	public final InstancenameContext instancename() throws RecognitionException {
		InstancenameContext _localctx = new InstancenameContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_instancename);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(176);
			match(IDENT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public FormatstringContext formatstring() {
			return getRuleContext(FormatstringContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).enterStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).exitStatement(this);
		}
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_statement);
		int _la;
		try {
			setState(196);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENT:
			case NUM:
				enterOuterAlt(_localctx, 1);
				{
				setState(178);
				name(0);
				setState(179);
				match(T__12);
				setState(180);
				expression(0);
				setState(181);
				match(T__13);
				}
				break;
			case T__21:
				enterOuterAlt(_localctx, 2);
				{
				setState(183);
				match(T__21);
				setState(184);
				match(T__1);
				setState(185);
				formatstring();
				setState(190);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__6) {
					{
					{
					setState(186);
					match(T__6);
					setState(187);
					expression(0);
					}
					}
					setState(192);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(193);
				match(T__2);
				setState(194);
				match(T__13);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FormatstringContext extends ParserRuleContext {
		public List<FormatstringpartContext> formatstringpart() {
			return getRuleContexts(FormatstringpartContext.class);
		}
		public FormatstringpartContext formatstringpart(int i) {
			return getRuleContext(FormatstringpartContext.class,i);
		}
		public FormatstringContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_formatstring; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).enterFormatstring(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).exitFormatstring(this);
		}
	}

	public final FormatstringContext formatstring() throws RecognitionException {
		FormatstringContext _localctx = new FormatstringContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_formatstring);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(198);
			match(T__22);
			{
			setState(202);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__23 || _la==ALPHA) {
				{
				{
				setState(199);
				formatstringpart();
				}
				}
				setState(204);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
			setState(205);
			match(T__22);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FormatstringpartContext extends ParserRuleContext {
		public TerminalNode ALPHA() { return getToken(SmeilParser.ALPHA, 0); }
		public FormatstringpartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_formatstringpart; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).enterFormatstringpart(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).exitFormatstringpart(this);
		}
	}

	public final FormatstringpartContext formatstringpart() throws RecognitionException {
		FormatstringpartContext _localctx = new FormatstringpartContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_formatstringpart);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(207);
			_la = _input.LA(1);
			if ( !(_la==T__23 || _la==ALPHA) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public NameContext name() {
			return getRuleContext(NameContext.class,0);
		}
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public BinopContext binop() {
			return getRuleContext(BinopContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).enterExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).exitExpression(this);
		}
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 38;
		enterRecursionRule(_localctx, 38, RULE_expression, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(210);
			name(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(218);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ExpressionContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expression);
					setState(212);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(213);
					binop();
					setState(214);
					expression(2);
					}
					} 
				}
				setState(220);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class BinopContext extends ParserRuleContext {
		public BinopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_binop; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).enterBinop(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).exitBinop(this);
		}
	}

	public final BinopContext binop() throws RecognitionException {
		BinopContext _localctx = new BinopContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_binop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(221);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__24) | (1L << T__25) | (1L << T__26) | (1L << T__27) | (1L << T__28) | (1L << T__29) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << T__33) | (1L << T__34) | (1L << T__35) | (1L << T__36) | (1L << T__37) | (1L << T__38) | (1L << T__39) | (1L << T__40) | (1L << T__41))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class UnopContext extends ParserRuleContext {
		public UnopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unop; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).enterUnop(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).exitUnop(this);
		}
	}

	public final UnopContext unop() throws RecognitionException {
		UnopContext _localctx = new UnopContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_unop);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(223);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__24) | (1L << T__25) | (1L << T__42) | (1L << T__43))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LiteralContext extends ParserRuleContext {
		public TerminalNode NUM() { return getToken(SmeilParser.NUM, 0); }
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).enterLiteral(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).exitLiteral(this);
		}
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_literal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(225);
			match(NUM);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NameContext extends ParserRuleContext {
		public TerminalNode IDENT() { return getToken(SmeilParser.IDENT, 0); }
		public TerminalNode NUM() { return getToken(SmeilParser.NUM, 0); }
		public List<NameContext> name() {
			return getRuleContexts(NameContext.class);
		}
		public NameContext name(int i) {
			return getRuleContext(NameContext.class,i);
		}
		public NameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_name; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).enterName(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).exitName(this);
		}
	}

	public final NameContext name() throws RecognitionException {
		return name(0);
	}

	private NameContext name(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		NameContext _localctx = new NameContext(_ctx, _parentState);
		NameContext _prevctx = _localctx;
		int _startState = 46;
		enterRecursionRule(_localctx, 46, RULE_name, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(230);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENT:
				{
				setState(228);
				match(IDENT);
				}
				break;
			case NUM:
				{
				setState(229);
				match(NUM);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(237);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new NameContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_name);
					setState(232);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(233);
					match(T__20);
					setState(234);
					name(2);
					}
					} 
				}
				setState(239);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 19:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		case 23:
			return name_sempred((NameContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean name_sempred(NameContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\63\u00f3\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\3\2\3\2\7\2\65\n\2\f\2\16\28\13\2\3\3\3\3\5\3<\n\3\3\4\3\4\3\4\3\4\5"+
		"\4B\n\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5M\n\5\3\5\3\5\7\5Q\n\5"+
		"\f\5\16\5T\13\5\3\5\3\5\7\5X\n\5\f\5\16\5[\13\5\3\5\3\5\3\6\7\6`\n\6\f"+
		"\6\16\6c\13\6\3\7\3\7\5\7g\n\7\3\b\3\b\3\b\7\bl\n\b\f\b\16\bo\13\b\3\t"+
		"\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\5\13|\n\13\3\13\5\13\177"+
		"\n\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\5\r\u0089\n\r\3\r\3\r\3\r\3\r"+
		"\3\r\3\r\3\r\3\16\3\16\7\16\u0094\n\16\f\16\16\16\u0097\13\16\3\17\3\17"+
		"\3\17\3\17\3\17\5\17\u009e\n\17\3\17\5\17\u00a1\n\17\3\17\3\17\3\20\3"+
		"\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00ae\n\20\3\20\3\20\3\20"+
		"\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\7\22\u00bf"+
		"\n\22\f\22\16\22\u00c2\13\22\3\22\3\22\3\22\5\22\u00c7\n\22\3\23\3\23"+
		"\7\23\u00cb\n\23\f\23\16\23\u00ce\13\23\3\23\3\23\3\24\3\24\3\25\3\25"+
		"\3\25\3\25\3\25\3\25\3\25\7\25\u00db\n\25\f\25\16\25\u00de\13\25\3\26"+
		"\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\31\5\31\u00e9\n\31\3\31\3\31\3\31"+
		"\7\31\u00ee\n\31\f\31\16\31\u00f1\13\31\3\31\2\4(\60\32\2\4\6\b\n\f\16"+
		"\20\22\24\26\30\32\34\36 \"$&(*,.\60\2\6\3\2\n\f\4\2\32\32\61\61\3\2\33"+
		",\4\2\33\34-.\2\u00f0\2\62\3\2\2\2\4;\3\2\2\2\6=\3\2\2\2\bH\3\2\2\2\n"+
		"a\3\2\2\2\ff\3\2\2\2\16h\3\2\2\2\20p\3\2\2\2\22s\3\2\2\2\24u\3\2\2\2\26"+
		"\u0082\3\2\2\2\30\u0088\3\2\2\2\32\u0091\3\2\2\2\34\u0098\3\2\2\2\36\u00a4"+
		"\3\2\2\2 \u00b2\3\2\2\2\"\u00c6\3\2\2\2$\u00c8\3\2\2\2&\u00d1\3\2\2\2"+
		"(\u00d3\3\2\2\2*\u00df\3\2\2\2,\u00e1\3\2\2\2.\u00e3\3\2\2\2\60\u00e8"+
		"\3\2\2\2\62\66\5\4\3\2\63\65\5\4\3\2\64\63\3\2\2\2\658\3\2\2\2\66\64\3"+
		"\2\2\2\66\67\3\2\2\2\67\3\3\2\2\28\66\3\2\2\29<\5\6\4\2:<\5\b\5\2;9\3"+
		"\2\2\2;:\3\2\2\2<\5\3\2\2\2=>\7\3\2\2>?\7\60\2\2?A\7\4\2\2@B\5\16\b\2"+
		"A@\3\2\2\2AB\3\2\2\2BC\3\2\2\2CD\7\5\2\2DE\7\6\2\2EF\5\n\6\2FG\7\7\2\2"+
		"G\7\3\2\2\2HI\7\b\2\2IJ\7\60\2\2JL\7\4\2\2KM\5\16\b\2LK\3\2\2\2LM\3\2"+
		"\2\2MN\3\2\2\2NR\7\5\2\2OQ\5\f\7\2PO\3\2\2\2QT\3\2\2\2RP\3\2\2\2RS\3\2"+
		"\2\2SU\3\2\2\2TR\3\2\2\2UY\7\6\2\2VX\5\"\22\2WV\3\2\2\2X[\3\2\2\2YW\3"+
		"\2\2\2YZ\3\2\2\2Z\\\3\2\2\2[Y\3\2\2\2\\]\7\7\2\2]\t\3\2\2\2^`\5\36\20"+
		"\2_^\3\2\2\2`c\3\2\2\2a_\3\2\2\2ab\3\2\2\2b\13\3\2\2\2ca\3\2\2\2dg\5\24"+
		"\13\2eg\5\30\r\2fd\3\2\2\2fe\3\2\2\2g\r\3\2\2\2hm\5\20\t\2ij\7\t\2\2j"+
		"l\5\20\t\2ki\3\2\2\2lo\3\2\2\2mk\3\2\2\2mn\3\2\2\2n\17\3\2\2\2om\3\2\2"+
		"\2pq\5\22\n\2qr\7\60\2\2r\21\3\2\2\2st\t\2\2\2t\23\3\2\2\2uv\7\r\2\2v"+
		"w\7\60\2\2wx\7\16\2\2x{\7/\2\2yz\7\17\2\2z|\5(\25\2{y\3\2\2\2{|\3\2\2"+
		"\2|~\3\2\2\2}\177\5\26\f\2~}\3\2\2\2~\177\3\2\2\2\177\u0080\3\2\2\2\u0080"+
		"\u0081\7\20\2\2\u0081\25\3\2\2\2\u0082\u0083\7\21\2\2\u0083\u0084\5(\25"+
		"\2\u0084\u0085\7\22\2\2\u0085\u0086\5(\25\2\u0086\27\3\2\2\2\u0087\u0089"+
		"\7\23\2\2\u0088\u0087\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008a\3\2\2\2"+
		"\u008a\u008b\7\24\2\2\u008b\u008c\7\60\2\2\u008c\u008d\7\6\2\2\u008d\u008e"+
		"\5\32\16\2\u008e\u008f\7\7\2\2\u008f\u0090\7\20\2\2\u0090\31\3\2\2\2\u0091"+
		"\u0095\5\34\17\2\u0092\u0094\5\34\17\2\u0093\u0092\3\2\2\2\u0094\u0097"+
		"\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096\33\3\2\2\2\u0097"+
		"\u0095\3\2\2\2\u0098\u0099\7\60\2\2\u0099\u009a\7\16\2\2\u009a\u009d\7"+
		"/\2\2\u009b\u009c\7\17\2\2\u009c\u009e\5(\25\2\u009d\u009b\3\2\2\2\u009d"+
		"\u009e\3\2\2\2\u009e\u00a0\3\2\2\2\u009f\u00a1\5\26\f\2\u00a0\u009f\3"+
		"\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3\7\20\2\2\u00a3"+
		"\35\3\2\2\2\u00a4\u00a5\7\25\2\2\u00a5\u00a6\5 \21\2\u00a6\u00a7\7\26"+
		"\2\2\u00a7\u00a8\7\60\2\2\u00a8\u00ad\7\4\2\2\u00a9\u00aa\5\60\31\2\u00aa"+
		"\u00ab\7\27\2\2\u00ab\u00ac\5\60\31\2\u00ac\u00ae\3\2\2\2\u00ad\u00a9"+
		"\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b0\7\5\2\2\u00b0"+
		"\u00b1\7\20\2\2\u00b1\37\3\2\2\2\u00b2\u00b3\7\60\2\2\u00b3!\3\2\2\2\u00b4"+
		"\u00b5\5\60\31\2\u00b5\u00b6\7\17\2\2\u00b6\u00b7\5(\25\2\u00b7\u00b8"+
		"\7\20\2\2\u00b8\u00c7\3\2\2\2\u00b9\u00ba\7\30\2\2\u00ba\u00bb\7\4\2\2"+
		"\u00bb\u00c0\5$\23\2\u00bc\u00bd\7\t\2\2\u00bd\u00bf\5(\25\2\u00be\u00bc"+
		"\3\2\2\2\u00bf\u00c2\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1"+
		"\u00c3\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c3\u00c4\7\5\2\2\u00c4\u00c5\7\20"+
		"\2\2\u00c5\u00c7\3\2\2\2\u00c6\u00b4\3\2\2\2\u00c6\u00b9\3\2\2\2\u00c7"+
		"#\3\2\2\2\u00c8\u00cc\7\31\2\2\u00c9\u00cb\5&\24\2\u00ca\u00c9\3\2\2\2"+
		"\u00cb\u00ce\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00cf"+
		"\3\2\2\2\u00ce\u00cc\3\2\2\2\u00cf\u00d0\7\31\2\2\u00d0%\3\2\2\2\u00d1"+
		"\u00d2\t\3\2\2\u00d2\'\3\2\2\2\u00d3\u00d4\b\25\1\2\u00d4\u00d5\5\60\31"+
		"\2\u00d5\u00dc\3\2\2\2\u00d6\u00d7\f\3\2\2\u00d7\u00d8\5*\26\2\u00d8\u00d9"+
		"\5(\25\4\u00d9\u00db\3\2\2\2\u00da\u00d6\3\2\2\2\u00db\u00de\3\2\2\2\u00dc"+
		"\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd)\3\2\2\2\u00de\u00dc\3\2\2\2"+
		"\u00df\u00e0\t\4\2\2\u00e0+\3\2\2\2\u00e1\u00e2\t\5\2\2\u00e2-\3\2\2\2"+
		"\u00e3\u00e4\7\62\2\2\u00e4/\3\2\2\2\u00e5\u00e6\b\31\1\2\u00e6\u00e9"+
		"\7\60\2\2\u00e7\u00e9\7\62\2\2\u00e8\u00e5\3\2\2\2\u00e8\u00e7\3\2\2\2"+
		"\u00e9\u00ef\3\2\2\2\u00ea\u00eb\f\3\2\2\u00eb\u00ec\7\27\2\2\u00ec\u00ee"+
		"\5\60\31\4\u00ed\u00ea\3\2\2\2\u00ee\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2"+
		"\u00ef\u00f0\3\2\2\2\u00f0\61\3\2\2\2\u00f1\u00ef\3\2\2\2\30\66;ALRYa"+
		"fm{~\u0088\u0095\u009d\u00a0\u00ad\u00c0\u00c6\u00cc\u00dc\u00e8\u00ef";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}