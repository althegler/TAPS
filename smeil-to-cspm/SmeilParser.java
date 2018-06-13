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
		T__24=25, T__25=26, T__26=27, T__27=28, TYPENAME=29, IDENT=30, ALPHA=31, 
		NUM=32, WHITESPACE=33;
	public static final int
		RULE_module = 0, RULE_entity = 1, RULE_network = 2, RULE_networkdecl = 3, 
		RULE_instance = 4, RULE_instancename = 5, RULE_process = 6, RULE_declaration = 7, 
		RULE_params = 8, RULE_param = 9, RULE_direction = 10, RULE_statement = 11, 
		RULE_formatstring = 12, RULE_formatstringpart = 13, RULE_busdecl = 14, 
		RULE_bussignaldecls = 15, RULE_bussignaldecl = 16, RULE_vardecl = 17, 
		RULE_ranges = 18, RULE_expression = 19, RULE_binop = 20, RULE_name = 21;
	public static final String[] ruleNames = {
		"module", "entity", "network", "networkdecl", "instance", "instancename", 
		"process", "declaration", "params", "param", "direction", "statement", 
		"formatstring", "formatstringpart", "busdecl", "bussignaldecls", "bussignaldecl", 
		"vardecl", "ranges", "expression", "binop", "name"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'network'", "'('", "')'", "'{'", "'}'", "'instance'", "'of'", "'.'", 
		"';'", "'proc'", "','", "'in'", "'out'", "'const'", "'='", "'trace'", 
		"'\"'", "'{}'", "'exposed'", "'bus'", "':'", "'var'", "'range'", "'to'", 
		"'/'", "'%'", "'+'", "'-'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, "TYPENAME", "IDENT", "ALPHA", "NUM", "WHITESPACE"
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
			setState(44);
			entity();
			setState(48);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__0 || _la==T__9) {
				{
				{
				setState(45);
				entity();
				}
				}
				setState(50);
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
		public List<ProcessContext> process() {
			return getRuleContexts(ProcessContext.class);
		}
		public ProcessContext process(int i) {
			return getRuleContext(ProcessContext.class,i);
		}
		public NetworkContext network() {
			return getRuleContext(NetworkContext.class,0);
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
			int _alt;
			setState(59);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__9:
				enterOuterAlt(_localctx, 1);
				{
				setState(51);
				process();
				setState(55);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(52);
						process();
						}
						} 
					}
					setState(57);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
				}
				}
				break;
			case T__0:
				enterOuterAlt(_localctx, 2);
				{
				setState(58);
				network();
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
			setState(61);
			match(T__0);
			setState(62);
			match(IDENT);
			setState(63);
			match(T__1);
			setState(65);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__11) | (1L << T__12) | (1L << T__13))) != 0)) {
				{
				setState(64);
				params();
				}
			}

			setState(67);
			match(T__2);
			setState(68);
			match(T__3);
			setState(69);
			networkdecl();
			setState(70);
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
		enterRule(_localctx, 6, RULE_networkdecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__5) {
				{
				{
				setState(72);
				instance();
				}
				}
				setState(77);
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
		enterRule(_localctx, 8, RULE_instance);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(78);
			match(T__5);
			setState(79);
			instancename();
			setState(80);
			match(T__6);
			setState(81);
			match(IDENT);
			setState(82);
			match(T__1);
			setState(87);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==IDENT || _la==NUM) {
				{
				setState(83);
				name(0);
				setState(84);
				match(T__7);
				setState(85);
				name(0);
				}
			}

			setState(89);
			match(T__2);
			setState(90);
			match(T__8);
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
		enterRule(_localctx, 10, RULE_instancename);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(92);
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
		enterRule(_localctx, 12, RULE_process);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(94);
			match(T__9);
			setState(95);
			match(IDENT);
			setState(96);
			match(T__1);
			setState(98);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__11) | (1L << T__12) | (1L << T__13))) != 0)) {
				{
				setState(97);
				params();
				}
			}

			setState(100);
			match(T__2);
			setState(104);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__18) | (1L << T__19) | (1L << T__21))) != 0)) {
				{
				{
				setState(101);
				declaration();
				}
				}
				setState(106);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(107);
			match(T__3);
			setState(111);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__15) | (1L << IDENT) | (1L << NUM))) != 0)) {
				{
				{
				setState(108);
				statement();
				}
				}
				setState(113);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(114);
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
		enterRule(_localctx, 14, RULE_declaration);
		try {
			setState(118);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__21:
				enterOuterAlt(_localctx, 1);
				{
				setState(116);
				vardecl();
				}
				break;
			case T__18:
			case T__19:
				enterOuterAlt(_localctx, 2);
				{
				setState(117);
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
		enterRule(_localctx, 16, RULE_params);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(120);
			param();
			setState(125);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__10) {
				{
				{
				setState(121);
				match(T__10);
				setState(122);
				param();
				}
				}
				setState(127);
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
		enterRule(_localctx, 18, RULE_param);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			direction();
			setState(129);
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
		enterRule(_localctx, 20, RULE_direction);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(131);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__11) | (1L << T__12) | (1L << T__13))) != 0)) ) {
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
		enterRule(_localctx, 22, RULE_statement);
		int _la;
		try {
			setState(151);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENT:
			case NUM:
				enterOuterAlt(_localctx, 1);
				{
				setState(133);
				name(0);
				setState(134);
				match(T__14);
				setState(135);
				expression(0);
				setState(136);
				match(T__8);
				}
				break;
			case T__15:
				enterOuterAlt(_localctx, 2);
				{
				setState(138);
				match(T__15);
				setState(139);
				match(T__1);
				setState(140);
				formatstring();
				setState(145);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__10) {
					{
					{
					setState(141);
					match(T__10);
					setState(142);
					expression(0);
					}
					}
					setState(147);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(148);
				match(T__2);
				setState(149);
				match(T__8);
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
		enterRule(_localctx, 24, RULE_formatstring);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(153);
			match(T__16);
			{
			setState(157);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__17 || _la==IDENT) {
				{
				{
				setState(154);
				formatstringpart();
				}
				}
				setState(159);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
			setState(160);
			match(T__16);
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
		public TerminalNode IDENT() { return getToken(SmeilParser.IDENT, 0); }
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
		enterRule(_localctx, 26, RULE_formatstringpart);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(162);
			_la = _input.LA(1);
			if ( !(_la==T__17 || _la==IDENT) ) {
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
		enterRule(_localctx, 28, RULE_busdecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(165);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__18) {
				{
				setState(164);
				match(T__18);
				}
			}

			setState(167);
			match(T__19);
			setState(168);
			match(IDENT);
			setState(169);
			match(T__3);
			setState(170);
			bussignaldecls();
			setState(171);
			match(T__4);
			setState(172);
			match(T__8);
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
		enterRule(_localctx, 30, RULE_bussignaldecls);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(174);
			bussignaldecl();
			setState(178);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==IDENT) {
				{
				{
				setState(175);
				bussignaldecl();
				}
				}
				setState(180);
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
		public RangesContext ranges() {
			return getRuleContext(RangesContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
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
		enterRule(_localctx, 32, RULE_bussignaldecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(181);
			match(IDENT);
			setState(182);
			match(T__20);
			setState(183);
			match(TYPENAME);
			setState(186);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__14) {
				{
				setState(184);
				match(T__14);
				setState(185);
				expression(0);
				}
			}

			setState(188);
			ranges();
			setState(189);
			match(T__8);
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
		public RangesContext ranges() {
			return getRuleContext(RangesContext.class,0);
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
		enterRule(_localctx, 34, RULE_vardecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(191);
			match(T__21);
			setState(192);
			match(IDENT);
			setState(193);
			match(T__20);
			setState(194);
			match(TYPENAME);
			setState(197);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__14) {
				{
				setState(195);
				match(T__14);
				setState(196);
				expression(0);
				}
			}

			setState(200);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__22) {
				{
				setState(199);
				ranges();
				}
			}

			setState(202);
			match(T__8);
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

	public static class RangesContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public RangesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ranges; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).enterRanges(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof SmeilListener ) ((SmeilListener)listener).exitRanges(this);
		}
	}

	public final RangesContext ranges() throws RecognitionException {
		RangesContext _localctx = new RangesContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_ranges);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(204);
			match(T__22);
			setState(205);
			expression(0);
			setState(206);
			match(T__23);
			setState(207);
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
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__24) | (1L << T__25) | (1L << T__26) | (1L << T__27))) != 0)) ) {
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
		int _startState = 42;
		enterRecursionRule(_localctx, 42, RULE_name, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(226);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENT:
				{
				setState(224);
				match(IDENT);
				}
				break;
			case NUM:
				{
				setState(225);
				match(NUM);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(233);
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
					setState(228);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(229);
					match(T__7);
					setState(230);
					name(2);
					}
					} 
				}
				setState(235);
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
		case 21:
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3#\u00ef\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2\3\2\7\2\61\n\2"+
		"\f\2\16\2\64\13\2\3\3\3\3\7\38\n\3\f\3\16\3;\13\3\3\3\5\3>\n\3\3\4\3\4"+
		"\3\4\3\4\5\4D\n\4\3\4\3\4\3\4\3\4\3\4\3\5\7\5L\n\5\f\5\16\5O\13\5\3\6"+
		"\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6Z\n\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b"+
		"\3\b\3\b\5\be\n\b\3\b\3\b\7\bi\n\b\f\b\16\bl\13\b\3\b\3\b\7\bp\n\b\f\b"+
		"\16\bs\13\b\3\b\3\b\3\t\3\t\5\ty\n\t\3\n\3\n\3\n\7\n~\n\n\f\n\16\n\u0081"+
		"\13\n\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\7"+
		"\r\u0092\n\r\f\r\16\r\u0095\13\r\3\r\3\r\3\r\5\r\u009a\n\r\3\16\3\16\7"+
		"\16\u009e\n\16\f\16\16\16\u00a1\13\16\3\16\3\16\3\17\3\17\3\20\5\20\u00a8"+
		"\n\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\7\21\u00b3\n\21\f\21"+
		"\16\21\u00b6\13\21\3\22\3\22\3\22\3\22\3\22\5\22\u00bd\n\22\3\22\3\22"+
		"\3\22\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00c8\n\23\3\23\5\23\u00cb\n"+
		"\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3"+
		"\25\7\25\u00db\n\25\f\25\16\25\u00de\13\25\3\26\3\26\3\27\3\27\3\27\5"+
		"\27\u00e5\n\27\3\27\3\27\3\27\7\27\u00ea\n\27\f\27\16\27\u00ed\13\27\3"+
		"\27\2\4(,\30\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,\2\5\3\2\16"+
		"\20\4\2\24\24  \3\2\33\36\2\u00ee\2.\3\2\2\2\4=\3\2\2\2\6?\3\2\2\2\bM"+
		"\3\2\2\2\nP\3\2\2\2\f^\3\2\2\2\16`\3\2\2\2\20x\3\2\2\2\22z\3\2\2\2\24"+
		"\u0082\3\2\2\2\26\u0085\3\2\2\2\30\u0099\3\2\2\2\32\u009b\3\2\2\2\34\u00a4"+
		"\3\2\2\2\36\u00a7\3\2\2\2 \u00b0\3\2\2\2\"\u00b7\3\2\2\2$\u00c1\3\2\2"+
		"\2&\u00ce\3\2\2\2(\u00d3\3\2\2\2*\u00df\3\2\2\2,\u00e4\3\2\2\2.\62\5\4"+
		"\3\2/\61\5\4\3\2\60/\3\2\2\2\61\64\3\2\2\2\62\60\3\2\2\2\62\63\3\2\2\2"+
		"\63\3\3\2\2\2\64\62\3\2\2\2\659\5\16\b\2\668\5\16\b\2\67\66\3\2\2\28;"+
		"\3\2\2\29\67\3\2\2\29:\3\2\2\2:>\3\2\2\2;9\3\2\2\2<>\5\6\4\2=\65\3\2\2"+
		"\2=<\3\2\2\2>\5\3\2\2\2?@\7\3\2\2@A\7 \2\2AC\7\4\2\2BD\5\22\n\2CB\3\2"+
		"\2\2CD\3\2\2\2DE\3\2\2\2EF\7\5\2\2FG\7\6\2\2GH\5\b\5\2HI\7\7\2\2I\7\3"+
		"\2\2\2JL\5\n\6\2KJ\3\2\2\2LO\3\2\2\2MK\3\2\2\2MN\3\2\2\2N\t\3\2\2\2OM"+
		"\3\2\2\2PQ\7\b\2\2QR\5\f\7\2RS\7\t\2\2ST\7 \2\2TY\7\4\2\2UV\5,\27\2VW"+
		"\7\n\2\2WX\5,\27\2XZ\3\2\2\2YU\3\2\2\2YZ\3\2\2\2Z[\3\2\2\2[\\\7\5\2\2"+
		"\\]\7\13\2\2]\13\3\2\2\2^_\7 \2\2_\r\3\2\2\2`a\7\f\2\2ab\7 \2\2bd\7\4"+
		"\2\2ce\5\22\n\2dc\3\2\2\2de\3\2\2\2ef\3\2\2\2fj\7\5\2\2gi\5\20\t\2hg\3"+
		"\2\2\2il\3\2\2\2jh\3\2\2\2jk\3\2\2\2km\3\2\2\2lj\3\2\2\2mq\7\6\2\2np\5"+
		"\30\r\2on\3\2\2\2ps\3\2\2\2qo\3\2\2\2qr\3\2\2\2rt\3\2\2\2sq\3\2\2\2tu"+
		"\7\7\2\2u\17\3\2\2\2vy\5$\23\2wy\5\36\20\2xv\3\2\2\2xw\3\2\2\2y\21\3\2"+
		"\2\2z\177\5\24\13\2{|\7\r\2\2|~\5\24\13\2}{\3\2\2\2~\u0081\3\2\2\2\177"+
		"}\3\2\2\2\177\u0080\3\2\2\2\u0080\23\3\2\2\2\u0081\177\3\2\2\2\u0082\u0083"+
		"\5\26\f\2\u0083\u0084\7 \2\2\u0084\25\3\2\2\2\u0085\u0086\t\2\2\2\u0086"+
		"\27\3\2\2\2\u0087\u0088\5,\27\2\u0088\u0089\7\21\2\2\u0089\u008a\5(\25"+
		"\2\u008a\u008b\7\13\2\2\u008b\u009a\3\2\2\2\u008c\u008d\7\22\2\2\u008d"+
		"\u008e\7\4\2\2\u008e\u0093\5\32\16\2\u008f\u0090\7\r\2\2\u0090\u0092\5"+
		"(\25\2\u0091\u008f\3\2\2\2\u0092\u0095\3\2\2\2\u0093\u0091\3\2\2\2\u0093"+
		"\u0094\3\2\2\2\u0094\u0096\3\2\2\2\u0095\u0093\3\2\2\2\u0096\u0097\7\5"+
		"\2\2\u0097\u0098\7\13\2\2\u0098\u009a\3\2\2\2\u0099\u0087\3\2\2\2\u0099"+
		"\u008c\3\2\2\2\u009a\31\3\2\2\2\u009b\u009f\7\23\2\2\u009c\u009e\5\34"+
		"\17\2\u009d\u009c\3\2\2\2\u009e\u00a1\3\2\2\2\u009f\u009d\3\2\2\2\u009f"+
		"\u00a0\3\2\2\2\u00a0\u00a2\3\2\2\2\u00a1\u009f\3\2\2\2\u00a2\u00a3\7\23"+
		"\2\2\u00a3\33\3\2\2\2\u00a4\u00a5\t\3\2\2\u00a5\35\3\2\2\2\u00a6\u00a8"+
		"\7\25\2\2\u00a7\u00a6\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00a9\3\2\2\2"+
		"\u00a9\u00aa\7\26\2\2\u00aa\u00ab\7 \2\2\u00ab\u00ac\7\6\2\2\u00ac\u00ad"+
		"\5 \21\2\u00ad\u00ae\7\7\2\2\u00ae\u00af\7\13\2\2\u00af\37\3\2\2\2\u00b0"+
		"\u00b4\5\"\22\2\u00b1\u00b3\5\"\22\2\u00b2\u00b1\3\2\2\2\u00b3\u00b6\3"+
		"\2\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5!\3\2\2\2\u00b6\u00b4"+
		"\3\2\2\2\u00b7\u00b8\7 \2\2\u00b8\u00b9\7\27\2\2\u00b9\u00bc\7\37\2\2"+
		"\u00ba\u00bb\7\21\2\2\u00bb\u00bd\5(\25\2\u00bc\u00ba\3\2\2\2\u00bc\u00bd"+
		"\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00bf\5&\24\2\u00bf\u00c0\7\13\2\2"+
		"\u00c0#\3\2\2\2\u00c1\u00c2\7\30\2\2\u00c2\u00c3\7 \2\2\u00c3\u00c4\7"+
		"\27\2\2\u00c4\u00c7\7\37\2\2\u00c5\u00c6\7\21\2\2\u00c6\u00c8\5(\25\2"+
		"\u00c7\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00ca\3\2\2\2\u00c9\u00cb"+
		"\5&\24\2\u00ca\u00c9\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc"+
		"\u00cd\7\13\2\2\u00cd%\3\2\2\2\u00ce\u00cf\7\31\2\2\u00cf\u00d0\5(\25"+
		"\2\u00d0\u00d1\7\32\2\2\u00d1\u00d2\5(\25\2\u00d2\'\3\2\2\2\u00d3\u00d4"+
		"\b\25\1\2\u00d4\u00d5\5,\27\2\u00d5\u00dc\3\2\2\2\u00d6\u00d7\f\3\2\2"+
		"\u00d7\u00d8\5*\26\2\u00d8\u00d9\5(\25\4\u00d9\u00db\3\2\2\2\u00da\u00d6"+
		"\3\2\2\2\u00db\u00de\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd"+
		")\3\2\2\2\u00de\u00dc\3\2\2\2\u00df\u00e0\t\4\2\2\u00e0+\3\2\2\2\u00e1"+
		"\u00e2\b\27\1\2\u00e2\u00e5\7 \2\2\u00e3\u00e5\7\"\2\2\u00e4\u00e1\3\2"+
		"\2\2\u00e4\u00e3\3\2\2\2\u00e5\u00eb\3\2\2\2\u00e6\u00e7\f\3\2\2\u00e7"+
		"\u00e8\7\n\2\2\u00e8\u00ea\5,\27\4\u00e9\u00e6\3\2\2\2\u00ea\u00ed\3\2"+
		"\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec-\3\2\2\2\u00ed\u00eb"+
		"\3\2\2\2\30\629=CMYdjqx\177\u0093\u0099\u009f\u00a7\u00b4\u00bc\u00c7"+
		"\u00ca\u00dc\u00e4\u00eb";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}