// Generated from Smeil.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link SmeilParser}.
 */
public interface SmeilListener extends ParseTreeListener {
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
	 * Enter a parse tree produced by {@link SmeilParser#typename}.
	 * @param ctx the parse tree
	 */
	void enterTypename(SmeilParser.TypenameContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmeilParser#typename}.
	 * @param ctx the parse tree
	 */
	void exitTypename(SmeilParser.TypenameContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmeilParser#ranges}.
	 * @param ctx the parse tree
	 */
	void enterRanges(SmeilParser.RangesContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmeilParser#ranges}.
	 * @param ctx the parse tree
	 */
	void exitRanges(SmeilParser.RangesContext ctx);
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
	 * Enter a parse tree produced by {@link SmeilParser#name}.
	 * @param ctx the parse tree
	 */
	void enterName(SmeilParser.NameContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmeilParser#name}.
	 * @param ctx the parse tree
	 */
	void exitName(SmeilParser.NameContext ctx);
	/**
	 * Enter a parse tree produced by {@link SmeilParser#ident}.
	 * @param ctx the parse tree
	 */
	void enterIdent(SmeilParser.IdentContext ctx);
	/**
	 * Exit a parse tree produced by {@link SmeilParser#ident}.
	 * @param ctx the parse tree
	 */
	void exitIdent(SmeilParser.IdentContext ctx);
}