---
type: smite-build
god: Kali
mode: Conquest
builds:
- source: community
  aspect: Aspect of Unbound Destruction
  aspect_pick_rate: 0.3
  aspect_win_rate: 0.59
  slot_order:
  - name: Tyrfing
    pick_rate: 0.41
    win_rate: 0.56
    alternates:
    - name: Book of Thoth
      pick_rate: 0.12
      win_rate: 0.49
    - name: Devourer's Gauntlet
      pick_rate: 0.12
      win_rate: 0.53
  - name: Hastened Fatalis
    pick_rate: 0.12
    win_rate: 0.59
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.12
      win_rate: 0.64
    - name: Dagger of Frenzy
      pick_rate: 0.08
      win_rate: 0.48
  - name: Silverbranch Bow
    pick_rate: 0.16
    win_rate: 0.56
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.12
      win_rate: 0.61
    - name: Hastened Fatalis
      pick_rate: 0.11
      win_rate: 0.5
  - name: Odysseus' Bow
    pick_rate: 0.13
    win_rate: 0.66
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.11
      win_rate: 0.68
    - name: The Executioner
      pick_rate: 0.1
      win_rate: 0.54
  - name: The Executioner
    pick_rate: 0.13
    win_rate: 0.57
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.09
      win_rate: 0.52
    - name: Rod of Tahuti
      pick_rate: 0.06
      win_rate: 0.5
  - name: Blinking Abyss
    pick_rate: 0.08
    win_rate: 0.68
    alternates:
    - name: Bow
      pick_rate: 0.07
      win_rate: 0.5
    - name: Manchu Bow
      pick_rate: 0.07
      win_rate: 0.63
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.25
    win_rate: 0.6
  - name: Archmage's Gem
    pick_rate: 0.12
    win_rate: 0.56
  - name: Death's Embrace
    pick_rate: 0.11
    win_rate: 0.53
  source_url: https://smitebrain.com/gods/kali/
  last_verified: '2026-11-02'
  god_win_rate: 0.5346260387811634
  god_matches_won: 193
  god_matches_played: 361
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14484
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Tekko-Kagi
  - Silverbranch Bow
  - Titan's Bane
  flex_slots:
  - Silverbranch Bow
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Jotunn''s Revenge, Death Metal, Tekko-Kagi, Titan''s
    Bane, Lernaean Bow, Obsidian Shard, Bragi''s Harp, The Crusher, Hydra''s Lament,
    Spear of Desolation, Golden Blade, Heartseeker, Nimble Ring, Dominance, The Reaper,
    Soul Gem, Spear of the Magus, Toxic Blade, Arondight, Deathbringer, Demon Blade,
    Musashi''s Dual Swords, Gluttonous Grimoire, Bracer of The Abyss, Doom Orb, Transcendence,
    The World Stone, Riptalon, Avatar''s Parashu, Rage, Runeforged Hammer, Pendulum
    Blade, Dreamer''s Idol, Eros'' Bow, Qin''s Blade, Chronos'' Pendant, Berserker''s
    Shield, Avenging Blade, Eye of the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.69
      win: 0.56
      pick: 0.0
      fit: 0.49
    Tyrfing:
      total: 0.55
      efficiency: 0.5
      win: 0.56
      pick: 0.41
      fit: 0.68
    Death Metal:
      total: 0.55
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.51
    Tekko-Kagi:
      total: 0.55
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.69
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.52
      win: 0.56
      pick: 0.25
      fit: 0.53
    Titan's Bane:
      total: 0.52
      efficiency: 0.54
      win: 0.56
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Tyrfing
  - Silverbranch Bow
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Death Metal
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Tyrfing
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Jotunn''s Revenge, Death Metal, Spear of Desolation, Obsidian Shard,
    Hydra''s Lament, Tekko-Kagi, Soul Gem, Nimble Ring, Bragi''s Harp, Titan''s Bane,
    Spear of the Magus, Doom Orb, Heartseeker, Lernaean Bow, The World Stone, Dominance,
    Gluttonous Grimoire, Chronos'' Pendant, The Crusher, Arondight, Bracer of The
    Abyss, Ancient Signet, Heartwood Charm, Polynomicon, The Reaper, Transcendence,
    Dreamer''s Idol, Golden Blade, Gem of Focus, Eros'' Bow, Blood-Bound Book, Soul
    Reaver, Deathbringer, Musashi''s Dual Swords, Runeforged Hammer, The Cosmic Horror,
    Pendulum Blade, Toxic Blade, Book of Thoth.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.69
      win: 0.56
      pick: 0.0
      fit: 0.52
    Tyrfing:
      total: 0.52
      efficiency: 0.5
      win: 0.56
      pick: 0.41
      fit: 0.51
    Hydra's Lament:
      total: 0.52
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.49
    Death Metal:
      total: 0.55
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.54
    Spear of Desolation:
      total: 0.53
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.45
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.87
      win: 0.5
      pick: 0.13
      fit: 0.42
  community_ordered:
  - Tyrfing
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Death Metal
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Rod of Tahuti, Jotunn''s Revenge,
    Shield of the Phoenix, Soul Gem, Kinetic Cuirass, Death Metal, Shield Splitter,
    The Reaper, Genji''s Guard, Golden Blade, Runeforged Hammer, Tekko-Kagi, Yogi''s
    Necklace, Phoenix Feather, Ethereal Staff, Gluttonous Grimoire, Breastplate of
    Valor, Titan''s Bane, Freya''s Tears, Obsidian Shard, Blood-Bound Book, Pharaoh''s
    Curse, Lernaean Bow, Toxic Blade, Oni Hunter''s Garb, Riptalon, Erosion, Hydra''s
    Lament, Chandra''s Grace, Eye of Providence, Spear of Desolation, Shogun''s Ofuda,
    Midgardian Mail, Nimble Ring, Avenging Blade, Helm of Radiance, Eros'' Bow, Draconic
    Scale, Sphere of Negation.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.75
      win: 0.56
      pick: 0.0
      fit: 0.42
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.69
      win: 0.56
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.49
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.6
    Death Metal:
      total: 0.52
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.31
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Tekko-Kagi
  - Silverbranch Bow
  - Titan's Bane
  - Rod of Tahuti
  flex_slots:
  - Titan's Bane
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Tekko-Kagi, Titan''s Bane, Obsidian
    Shard, Death Metal, Spear of Desolation, The Crusher, Heartseeker, Soul Gem, Spear
    of the Magus, The Reaper, Toxic Blade, Gluttonous Grimoire, Doom Orb, Lernaean
    Bow, The World Stone, Avenging Blade, Hydra''s Lament, Avatar''s Parashu, Dreamer''s
    Idol, Nimble Ring, Riptalon, Bragi''s Harp, Pendulum Blade, Dominance, Golden
    Blade, The Cosmic Horror, Arondight, Deathbringer, Bracer of The Abyss, Musashi''s
    Dual Swords, Oath-Sworn Spear, Transcendence, Runeforged Hammer, Demon Blade,
    Chronos'' Pendant, Rage, Eros'' Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.69
      win: 0.56
      pick: 0.0
      fit: 0.61
    Death Metal:
      total: 0.53
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.39
    Tekko-Kagi:
      total: 0.56
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.76
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.52
      win: 0.56
      pick: 0.25
      fit: 0.64
    Titan's Bane:
      total: 0.54
      efficiency: 0.54
      win: 0.56
      pick: 0.0
      fit: 0.67
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.87
      win: 0.5
      pick: 0.13
      fit: 0.43
  community_ordered:
  - Silverbranch Bow
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Nimble Ring
  - Silverbranch Bow
  - Tekko-Kagi
  flex_slots:
  - Tekko-Kagi
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Jotunn''s Revenge, Nimble Ring, Tekko-Kagi, Death Metal,
    Soul Gem, Riptalon, Lernaean Bow, Golden Blade, The Reaper, Gluttonous Grimoire,
    Obsidian Shard, Titan''s Bane, Toxic Blade, Spear of Desolation, Bragi''s Harp,
    Dominance, Hydra''s Lament, The Crusher, Spear of the Magus, Qin''s Blade, Blood-Bound
    Book, Heartseeker, Bracer of The Abyss, Doom Orb, Arondight, Eros'' Bow, The World
    Stone, Sun Beam Bow, Berserker''s Shield, Transcendence, Demon Blade, Deathbringer,
    Bloodforge, Musashi''s Dual Swords, Chronos'' Pendant, Dreamer''s Idol, Runeforged
    Hammer, Bancroft''s Talon, Ancient Signet.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.69
      win: 0.56
      pick: 0.0
      fit: 0.31
    Tyrfing:
      total: 0.55
      efficiency: 0.5
      win: 0.56
      pick: 0.41
      fit: 0.67
    Death Metal:
      total: 0.52
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.32
    Nimble Ring:
      total: 0.53
      efficiency: 0.64
      win: 0.56
      pick: 0.0
      fit: 0.39
    Silverbranch Bow:
      total: 0.53
      efficiency: 0.52
      win: 0.56
      pick: 0.25
      fit: 0.57
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.53
  community_ordered:
  - Tyrfing
  - Silverbranch Bow
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Death Metal
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Hydra's Lament
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Rod of Tahuti,
    Spear of Desolation, Soul Gem, Hydra''s Lament, Death Metal, Chronos'' Pendant,
    Arondight, Tekko-Kagi, Obsidian Shard, Nimble Ring, Gem of Focus, Heartwood Charm,
    Titan''s Bane, Spear of the Magus, Lernaean Bow, Pendulum Blade, Bragi''s Harp,
    Gluttonous Grimoire, Doom Orb, The Crusher, Bracer of The Abyss, Totem of Death,
    Heartseeker, The World Stone, Damaru, Genji''s Guard, Dominance, Golden Blade,
    The Reaper, Toxic Blade, Dreamer''s Idol, Breastplate of Valor, Eros'' Bow, Ancient
    Signet, Blood-Bound Book, Polynomicon, Transcendence, Chandra''s Grace, Deathbringer.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.69
      win: 0.56
      pick: 0.0
      fit: 0.59
    Hydra's Lament:
      total: 0.53
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.55
    Death Metal:
      total: 0.53
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.34
    Spear of Desolation:
      total: 0.55
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.59
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.87
      win: 0.5
      pick: 0.13
      fit: 0.24
    Soul Gem:
      total: 0.54
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Tekko-Kagi
  - Titan's Bane
  - Rod of Tahuti
  flex_slots:
  - Tyrfing
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Death Metal, Tekko-Kagi,
    Titan''s Bane, Lernaean Bow, Obsidian Shard, Bragi''s Harp, The Crusher, Hydra''s
    Lament, Spear of Desolation, Golden Blade, Heartseeker, Nimble Ring, Dominance,
    The Reaper, Soul Gem, Spear of the Magus, Toxic Blade, Arondight, Deathbringer,
    Demon Blade, Musashi''s Dual Swords, Gluttonous Grimoire, Bracer of The Abyss,
    Doom Orb, Transcendence, The World Stone, Riptalon, Avatar''s Parashu, Rage, Runeforged
    Hammer, Pendulum Blade, Dreamer''s Idol, Eros'' Bow, Qin''s Blade, Chronos'' Pendant,
    Berserker''s Shield, Avenging Blade, Eye of the Storm.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.69
      win: 0.56
      pick: 0.0
      fit: 0.49
    Tyrfing:
      total: 0.55
      efficiency: 0.5
      win: 0.56
      pick: 0.41
      fit: 0.68
    Death Metal:
      total: 0.55
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.51
    Tekko-Kagi:
      total: 0.55
      efficiency: 0.55
      win: 0.56
      pick: 0.0
      fit: 0.69
    Titan's Bane:
      total: 0.52
      efficiency: 0.54
      win: 0.56
      pick: 0.0
      fit: 0.55
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.87
      win: 0.5
      pick: 0.13
      fit: 0.26
  community_ordered:
  - Tyrfing
  - Rod of Tahuti
  starter: *id001
---
