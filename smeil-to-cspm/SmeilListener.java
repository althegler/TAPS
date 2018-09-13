// Generated from Smeil.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link SmeilParser}.
 */
public interface SmeilListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link SmeilParser#module}.
	 * @param ctx the parse tree
	 */
	void enterModule(SmeilParser.ModuleContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmeilParser#module}.
	 * @param ctx the parse tree
	 */
	void exitModule(SmeilParser.ModuleContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmeilParser#entity}.
	 * @param ctx the parse tree
	 */
	void enterEntity(SmeilParser.EntityContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmeilParser#entity}.
	 * @param ctx the parse tree
	 */
	void exitEntity(SmeilParser.EntityContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmeilParser#network}.
	 * @param ctx the parse tree
	 */
	void enterNetwork(SmeilParser.NetworkContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmeilParser#network}.
	 * @param ctx the parse tree
	 */
	void exitNetwork(SmeilParser.NetworkContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmeilParser#process}.
	 * @param ctx the parse tree
	 */
	void enterProcess(SmeilParser.ProcessContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmeilParser#process}.
	 * @param ctx the parse tree
	 */
	void exitProcess(SmeilParser.ProcessContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmeilParser#networkdecl}.
	 * @param ctx the parse tree
	 */
	void enterNetworkdecl(SmeilParser.NetworkdeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmeilParser#networkdecl}.
	 * @param ctx the parse tree
	 */
	void exitNetworkdecl(SmeilParser.NetworkdeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmeilParser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration(SmeilParser.DeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmeilParser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration(SmeilParser.DeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmeilParser#params}.
	 * @param ctx the parse tree
	 */
	void enterParams(SmeilParser.ParamsContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmeilParser#params}.
	 * @param ctx the parse tree
	 */
	void exitParams(SmeilParser.ParamsContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmeilParser#param}.
	 * @param ctx the parse tree
	 */
	void enterParam(SmeilParser.ParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmeilParser#param}.
	 * @param ctx the parse tree
	 */
	void exitParam(SmeilParser.ParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmeilParser#direction}.
	 * @param ctx the parse tree
	 */
	void enterDirection(SmeilParser.DirectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmeilParser#direction}.
	 * @param ctx the parse tree
	 */
	void exitDirection(SmeilParser.DirectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmeilParser#vardecl}.
	 * @param ctx the parse tree
	 */
	void enterVardecl(SmeilParser.VardeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmeilParser#vardecl}.
	 * @param ctx the parse tree
	 */
	void exitVardecl(SmeilParser.VardeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmeilParser#range}.
	 * @param ctx the parse tree
	 */
	void enterRange(SmeilParser.RangeContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmeilParser#range}.
	 * @param ctx the parse tree
	 */
	void exitRange(SmeilParser.RangeContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmeilParser#busdecl}.
	 * @param ctx the parse tree
	 */
	void enterBusdecl(SmeilParser.BusdeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmeilParser#busdecl}.
	 * @param ctx the parse tree
	 */
	void exitBusdecl(SmeilParser.BusdeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmeilParser#bussignaldecls}.
	 * @param ctx the parse tree
	 */
	void enterBussignaldecls(SmeilParser.BussignaldeclsContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmeilParser#bussignaldecls}.
	 * @param ctx the parse tree
	 */
	void exitBussignaldecls(SmeilParser.BussignaldeclsContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmeilParser#bussignaldecl}.
	 * @param ctx the parse tree
	 */
	void enterBussignaldecl(SmeilParser.BussignaldeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmeilParser#bussignaldecl}.
	 * @param ctx the parse tree
	 */
	void exitBussignaldecl(SmeilParser.BussignaldeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmeilParser#instance}.
	 * @param ctx the parse tree
	 */
	void enterInstance(SmeilParser.InstanceContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmeilParser#instance}.
	 * @param ctx the parse tree
	 */
	void exitInstance(SmeilParser.InstanceContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmeilParser#instancename}.
	 * @param ctx the parse tree
	 */
	void enterInstancename(SmeilParser.InstancenameContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmeilParser#instancename}.
	 * @param ctx the parse tree
	 */
	void exitInstancename(SmeilParser.InstancenameContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmeilParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(SmeilParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmeilParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(SmeilParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmeilParser#formatstring}.
	 * @param ctx the parse tree
	 */
	void enterFormatstring(SmeilParser.FormatstringContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmeilParser#formatstring}.
	 * @param ctx the parse tree
	 */
	void exitFormatstring(SmeilParser.FormatstringContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmeilParser#formatstringpart}.
	 * @param ctx the parse tree
	 */
	void enterFormatstringpart(SmeilParser.FormatstringpartContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmeilParser#formatstringpart}.
	 * @param ctx the parse tree
	 */
	void exitFormatstringpart(SmeilParser.FormatstringpartContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmeilParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(SmeilParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmeilParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(SmeilParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmeilParser#binop}.
	 * @param ctx the parse tree
	 */
	void enterBinop(SmeilParser.BinopContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmeilParser#binop}.
	 * @param ctx the parse tree
	 */
	void exitBinop(SmeilParser.BinopContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmeilParser#unop}.
	 * @param ctx the parse tree
	 */
	void enterUnop(SmeilParser.UnopContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmeilParser#unop}.
	 * @param ctx the parse tree
	 */
	void exitUnop(SmeilParser.UnopContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmeilParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(SmeilParser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmeilParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(SmeilParser.LiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmeilParser#name}.
	 * @param ctx the parse tree
	 */
	void enterName(SmeilParser.NameContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmeilParser#name}.
	 * @param ctx the parse tree
	 */
	void exitName(SmeilParser.NameContext ctx);
}