<?php

/**
 * وحدة تحكم رسائل واتساب - WhatsApp message controller
 * واٹس ایپ پیغامات کنٹرولر
 */

namespace App\Http\Controllers;

use App\Services\WhatsAppService;
use Illuminate\Http\Request;
use Illuminate\Http\JsonResponse;

class WhatsAppController extends Controller
{
    /** @var WhatsAppService */
    private WhatsAppService $whatsAppService;

    /**
     * حقن الخدمة - Service injection - سروس انجیکشن
     */
    public function __construct(WhatsAppService $whatsAppService)
    {
        $this->whatsAppService = $whatsAppService;
    }

    /**
     * إرسال رسالة نصية - Send text message - ٹیکسٹ پیغام بھیجیں
     *
     * @param Request $request
     * @return JsonResponse
     */
    public function sendText(Request $request): JsonResponse
    {
        $validated = $request->validate([
            'to' => 'required|string',
            'body' => 'required|string',
        ]);

        $response = $this->whatsAppService->sendText(
            $validated['to'],
            $validated['body']
        );

        return response()->json($response);
    }

    /**
     * إرسال رسالة بأزرار - Send buttons message - بٹن پیغام بھیجیں
     *
     * @param Request $request
     * @return JsonResponse
     */
    public function sendButtons(Request $request): JsonResponse
    {
        $validated = $request->validate([
            'to' => 'required|string',
            'body' => 'required|string',
            'buttons' => 'required|array',
            'buttons.*.id' => 'required|string',
            'buttons.*.title' => 'required|string',
        ]);

        $response = $this->whatsAppService->sendButtons(
            $validated['to'],
            $validated['body'],
            $validated['buttons']
        );

        return response()->json($response);
    }

    /**
     * إرسال رسالة بقائمة - Send list message - لسٹ پیغام بھیجیں
     *
     * @param Request $request
     * @return JsonResponse
     */
    public function sendList(Request $request): JsonResponse
    {
        $validated = $request->validate([
            'to' => 'required|string',
            'header' => 'required|string',
            'body' => 'required|string',
            'footer' => 'required|string',
            'button' => 'required|string',
            'sections' => 'required|array',
            'sections.*.title' => 'required|string',
            'sections.*.rows' => 'required|array',
            'sections.*.rows.*.id' => 'required|string',
            'sections.*.rows.*.title' => 'required|string',
            'sections.*.rows.*.description' => 'nullable|string',
        ]);

        $response = $this->whatsAppService->sendList(
            $validated['to'],
            $validated['header'],
            $validated['body'],
            $validated['footer'],
            $validated['button'],
            $validated['sections']
        );

        return response()->json($response);
    }

    /**
     * إرسال صورة - Send image - تصویر بھیجیں
     *
     * @param Request $request
     * @return JsonResponse
     */
    public function sendImage(Request $request): JsonResponse
    {
        $validated = $request->validate([
            'to' => 'required|string',
            'link' => 'required|string|url',
            'caption' => 'nullable|string',
        ]);

        $response = $this->whatsAppService->sendImage(
            $validated['to'],
            $validated['link'],
            $validated['caption'] ?? null
        );

        return response()->json($response);
    }

    /**
     * إرسال فيديو - Send video - ویڈیو بھیجیں
     *
     * @param Request $request
     * @return JsonResponse
     */
    public function sendVideo(Request $request): JsonResponse
    {
        $validated = $request->validate([
            'to' => 'required|string',
            'link' => 'required|string|url',
            'caption' => 'nullable|string',
        ]);

        $response = $this->whatsAppService->sendVideo(
            $validated['to'],
            $validated['link'],
            $validated['caption'] ?? null
        );

        return response()->json($response);
    }

    /**
     * إرسال ملف صوتي - Send audio - آڈیو بھیجیں
     *
     * @param Request $request
     * @return JsonResponse
     */
    public function sendAudio(Request $request): JsonResponse
    {
        $validated = $request->validate([
            'to' => 'required|string',
            'link' => 'required|string|url',
        ]);

        $response = $this->whatsAppService->sendAudio(
            $validated['to'],
            $validated['link']
        );

        return response()->json($response);
    }

    /**
     * إرسال مستند - Send document - دستاویز بھیجیں
     *
     * @param Request $request
     * @return JsonResponse
     */
    public function sendDocument(Request $request): JsonResponse
    {
        $validated = $request->validate([
            'to' => 'required|string',
            'link' => 'required|string|url',
            'caption' => 'nullable|string',
            'filename' => 'nullable|string',
        ]);

        $response = $this->whatsAppService->sendDocument(
            $validated['to'],
            $validated['link'],
            $validated['caption'] ?? null,
            $validated['filename'] ?? null
        );

        return response()->json($response);
    }
}
