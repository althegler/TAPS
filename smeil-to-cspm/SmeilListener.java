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