---
type: smite-build
god: Tsukuyomi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Mangetsu
  aspect_pick_rate: 0.01
  aspect_win_rate: 0.5
  slot_order:
  - name: Transcendence
    pick_rate: 0.52
    win_rate: 0.58
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.3
      win_rate: 0.56
    - name: Hydra's Lament
      pick_rate: 0.08
      win_rate: 0.53
  - name: Hydra's Lament
    pick_rate: 0.22
    win_rate: 0.56
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.19
      win_rate: 0.57
    - name: Transcendence
      pick_rate: 0.19
      win_rate: 0.6
  - name: Book of Thoth
    pick_rate: 0.29
    win_rate: 0.61
    alternates:
    - name: The Reaper
      pick_rate: 0.1
      win_rate: 0.67
    - name: The Crusher
      pick_rate: 0.1
      win_rate: 0.61
  - name: Heartseeker
    pick_rate: 0.36
    win_rate: 0.55
    alternates:
    - name: The Crusher
      pick_rate: 0.1
      win_rate: 0.67
    - name: Jotunn's Revenge
      pick_rate: 0.09
      win_rate: 0.87
  - name: Titan's Bane
    pick_rate: 0.16
    win_rate: 0.68
    alternates:
    - name: Heartseeker
      pick_rate: 0.16
      win_rate: 0.83
    - name: The Reaper
      pick_rate: 0.08
      win_rate: 0.5
  - name: Skeggox
    pick_rate: 0.11
    win_rate: 0.55
    alternates:
    - name: Titan's Bane
      pick_rate: 0.08
      win_rate: 0.5
    - name: Lucerne Hammer
      pick_rate: 0.08
      win_rate: 0.63
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.47
    win_rate: 0.67
  - name: Bumba's Cudgel
    pick_rate: 0.31
    win_rate: 0.39
  - name: Bluestone Brooch
    pick_rate: 0.07
    win_rate: 0.69
  source_url: https://smitebrain.com/gods/tsukuyomi/
  last_verified: '2026-11-06'
  god_win_rate: 0.5683060109289617
  god_matches_won: 104
  god_matches_played: 183
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-06'
  god_matches_analyzed: 2859
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Transcendence
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Tyrfing
  - Transcendence
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Death Metal, Tyrfing, Tekko-Kagi, Bragi''s Harp, Spear
    of Desolation, Lernaean Bow, Dominance, Silverbranch Bow, Soul Gem, Golden Blade,
    Obsidian Shard, Spear of the Magus, Toxic Blade, Demon Blade, Bracer of The Abyss,
    Rage, Dreamer''s Idol, Arondight, Avatar''s Parashu, Nimble Ring, Ancient Signet,
    Gluttonous Grimoire, Deathbringer, Polynomicon, Qin''s Blade, Riptalon, Doom Orb,
    Chronos'' Pendant, The World Stone, Pendulum Blade, Runeforged Hammer, Blood-Bound
    Book, Dagger of Frenzy.'
  slot_scores:
    Transcendence:
      total: 0.5
      efficiency: 0.5
      win: 0.58
      pick: 0.52
      fit: 0.24
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.56
      pick: 0.3
      fit: 0.49
    Tyrfing:
      total: 0.55
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.69
    Death Metal:
      total: 0.55
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.51
    The Crusher:
      total: 0.57
      efficiency: 0.51
      win: 0.67
      pick: 0.17
      fit: 0.54
    Titan's Bane:
      total: 0.57
      efficiency: 0.48
      win: 0.68
      pick: 0.35
      fit: 0.54
  community_ordered:
  - Transcendence
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Death Metal
  - The Crusher
  - Titan's Bane
  - Rod of Tahuti
  flex_slots:
  - The Crusher
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Death Metal, Spear of Desolation, Soul Gem, Bragi''s Harp, Tyrfing,
    Ancient Signet, Obsidian Shard, Polynomicon, Spear of the Magus, Dominance, Tekko-Kagi,
    Chronos'' Pendant, Doom Orb, Dreamer''s Idol, Bracer of The Abyss, The World Stone,
    Heartwood Charm, Gluttonous Grimoire, Lernaean Bow, Nimble Ring, Soul Reaver,
    Arondight, Blood-Bound Book, Gem of Focus, Silverbranch Bow, Golden Blade, Avatar''s
    Parashu, Rage, The Cosmic Horror, Bancroft''s Talon, Pendulum Blade, Totem of
    Death.'
  slot_scores:
    Book of Thoth:
      total: 0.51
      efficiency: 0.48
      win: 0.61
      pick: 0.45
      fit: 0.28
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.56
      pick: 0.3
      fit: 0.52
    Death Metal:
      total: 0.56
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.54
    The Crusher:
      total: 0.55
      efficiency: 0.51
      win: 0.67
      pick: 0.17
      fit: 0.44
    Titan's Bane:
      total: 0.56
      efficiency: 0.48
      win: 0.68
      pick: 0.35
      fit: 0.44
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.82
      win: 0.57
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Book of Thoth
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Transcendence
  - Book of Thoth
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  - Rod of Tahuti
  flex_slots:
  - Book of Thoth
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Tahuti, Spear of Desolation, Death Metal, Soul Gem, Obsidian Shard,
    Tyrfing, Spear of the Magus, Tekko-Kagi, Bragi''s Harp, Dreamer''s Idol, Chronos''
    Pendant, Gluttonous Grimoire, Ancient Signet, Silverbranch Bow, Doom Orb, Polynomicon,
    The World Stone, Arondight, Bracer of The Abyss, Lernaean Bow, Dominance, Nimble
    Ring, Gem of Focus, Heartwood Charm, Pendulum Blade, Toxic Blade, Avatar''s Parashu,
    Blood-Bound Book, The Cosmic Horror, Golden Blade, Soul Reaver, Riptalon, Totem
    of Death, Rage, Damaru.'
  slot_scores:
    Transcendence:
      total: 0.48
      efficiency: 0.5
      win: 0.58
      pick: 0.52
      fit: 0.16
    Book of Thoth:
      total: 0.49
      efficiency: 0.48
      win: 0.61
      pick: 0.45
      fit: 0.16
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.56
      pick: 0.3
      fit: 0.56
    The Crusher:
      total: 0.56
      efficiency: 0.51
      win: 0.67
      pick: 0.17
      fit: 0.5
    Titan's Bane:
      total: 0.57
      efficiency: 0.48
      win: 0.68
      pick: 0.35
      fit: 0.5
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.82
      win: 0.57
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Transcendence
  - Book of Thoth
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - The Crusher
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Rod of Tahuti, Shield of the Phoenix,
    Kinetic Cuirass, Soul Gem, Genji''s Guard, Death Metal, Phoenix Feather, Yogi''s
    Necklace, Shield Splitter, Tyrfing, Ethereal Staff, Golden Blade, Freya''s Tears,
    Runeforged Hammer, Oni Hunter''s Garb, Blood-Bound Book, Draconic Scale, Gluttonous
    Grimoire, Breastplate of Valor, Chandra''s Grace, Spear of Desolation, Erosion,
    Eye of Providence, Midgardian Mail, Shogun''s Ofuda, Toxic Blade, Tekko-Kagi,
    Shifter''s Shield, Pharaoh''s Curse, Riptalon, Bragi''s Harp, Leviathan''s Hide,
    Regrowth Striders, Hide of the Nemean Lion.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.49
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.6
    The Crusher:
      total: 0.54
      efficiency: 0.51
      win: 0.67
      pick: 0.17
      fit: 0.37
    Titan's Bane:
      total: 0.55
      efficiency: 0.48
      win: 0.68
      pick: 0.35
      fit: 0.37
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.69
  community_ordered:
  - The Crusher
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Transcendence
  - Book of Thoth
  - Jotunn's Revenge
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Transcendence
  - Book of Thoth
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Tekko-Kagi, Spear of Desolation, Death Metal, Soul
    Gem, Tyrfing, Silverbranch Bow, Obsidian Shard, Spear of the Magus, Dreamer''s
    Idol, Toxic Blade, Gluttonous Grimoire, Avatar''s Parashu, Bragi''s Harp, Doom
    Orb, The World Stone, Lernaean Bow, Dominance, Riptalon, Avenging Blade, Pendulum
    Blade, Golden Blade, Ancient Signet, The Cosmic Horror, Bracer of The Abyss, Arondight,
    Polynomicon, Nimble Ring, Rage, Chronos'' Pendant, Qin''s Blade, Demon Blade,
    Deathbringer, Oath-Sworn Spear, Blood-Bound Book.'
  slot_scores:
    Transcendence:
      total: 0.49
      efficiency: 0.5
      win: 0.58
      pick: 0.52
      fit: 0.19
    Book of Thoth:
      total: 0.47
      efficiency: 0.48
      win: 0.61
      pick: 0.45
      fit: 0.05
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.56
      pick: 0.3
      fit: 0.6
    The Crusher:
      total: 0.59
      efficiency: 0.51
      win: 0.67
      pick: 0.17
      fit: 0.67
    Heartseeker:
      total: 0.55
      efficiency: 0.45
      win: 0.55
      pick: 0.6
      fit: 0.77
    Titan's Bane:
      total: 0.59
      efficiency: 0.48
      win: 0.68
      pick: 0.35
      fit: 0.67
  community_ordered:
  - Transcendence
  - Book of Thoth
  - Jotunn's Revenge
  - The Crusher
  - Heartseeker
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Nimble Ring
  - Silverbranch Bow
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Nimble Ring
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Tyrfing, Death Metal, Soul Gem, Nimble Ring, Silverbranch
    Bow, Riptalon, Tekko-Kagi, Bragi''s Harp, Spear of Desolation, Golden Blade, Gluttonous
    Grimoire, Lernaean Bow, Dominance, Toxic Blade, Blood-Bound Book, Qin''s Blade,
    Obsidian Shard, Bracer of The Abyss, Spear of the Magus, Ancient Signet, Polynomicon,
    Dreamer''s Idol, Dagger of Frenzy, Arondight, Chronos'' Pendant, Demon Blade,
    Doom Orb, Rage, Bancroft''s Talon, Avatar''s Parashu, Berserker''s Shield, The
    World Stone, Soul Reaver, Deathbringer.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.56
      pick: 0.3
      fit: 0.3
    Tyrfing:
      total: 0.54
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.66
    Nimble Ring:
      total: 0.51
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.39
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.49
      win: 0.57
      pick: 0.0
      fit: 0.56
    The Crusher:
      total: 0.54
      efficiency: 0.51
      win: 0.67
      pick: 0.17
      fit: 0.37
    Titan's Bane:
      total: 0.55
      efficiency: 0.48
      win: 0.68
      pick: 0.35
      fit: 0.37
  community_ordered:
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Spear of Desolation
  - The Crusher
  - Titan's Bane
  - Soul Gem
  flex_slots:
  - Hydra's Lament
  - The Crusher
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Spear of Desolation,
    Soul Gem, Death Metal, Chronos'' Pendant, Tyrfing, Arondight, Gem of Focus, Heartwood
    Charm, Obsidian Shard, Bragi''s Harp, Tekko-Kagi, Spear of the Magus, Ancient
    Signet, Damaru, Genji''s Guard, Silverbranch Bow, Pendulum Blade, Polynomicon,
    Totem of Death, Bracer of The Abyss, Dreamer''s Idol, Lernaean Bow, Dominance,
    Nimble Ring, Gluttonous Grimoire, Doom Orb, Blood-Bound Book, Breastplate of Valor,
    The World Stone, Golden Blade, Toxic Blade, Chandra''s Grace, Soul Reaver, Qin''s
    Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.56
      pick: 0.3
      fit: 0.59
    Hydra's Lament:
      total: 0.54
      efficiency: 0.55
      win: 0.56
      pick: 0.3
      fit: 0.55
    Spear of Desolation:
      total: 0.56
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.59
    The Crusher:
      total: 0.54
      efficiency: 0.51
      win: 0.67
      pick: 0.17
      fit: 0.34
    Titan's Bane:
      total: 0.54
      efficiency: 0.48
      win: 0.68
      pick: 0.35
      fit: 0.34
    Soul Gem:
      total: 0.55
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Crusher
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Transcendence
  - Book of Thoth
  - Jotunn's Revenge
  - Death Metal
  - Titan's Bane
  - Rod of Tahuti
  flex_slots:
  - Book of Thoth
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Rod of Tahuti, Death Metal, Spear of Desolation,
    Soul Gem, Bragi''s Harp, Obsidian Shard, Tyrfing, Spear of the Magus, Chronos''
    Pendant, Ancient Signet, Dreamer''s Idol, Polynomicon, Gluttonous Grimoire, Bracer
    of The Abyss, Tekko-Kagi, Nimble Ring, Doom Orb, The World Stone, Gem of Focus,
    Heartwood Charm, Blood-Bound Book, Lernaean Bow, Dominance, Silverbranch Bow,
    Arondight, Soul Reaver, The Cosmic Horror, Golden Blade, Totem of Death, Toxic
    Blade, Avatar''s Parashu, Pendulum Blade, Rage, Qin''s Blade.'
  slot_scores:
    Transcendence:
      total: 0.49
      efficiency: 0.5
      win: 0.58
      pick: 0.52
      fit: 0.16
    Book of Thoth:
      total: 0.5
      efficiency: 0.48
      win: 0.61
      pick: 0.45
      fit: 0.25
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.56
      pick: 0.3
      fit: 0.46
    Death Metal:
      total: 0.56
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.54
    Titan's Bane:
      total: 0.55
      efficiency: 0.48
      win: 0.68
      pick: 0.35
      fit: 0.43
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.82
      win: 0.57
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Transcendence
  - Book of Thoth
  - Jotunn's Revenge
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Spear of Desolation
  - The Crusher
  - Titan's Bane
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - Spear of Desolation
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Death Metal, Spear
    of Desolation, Bragi''s Harp, Tyrfing, Soul Gem, Obsidian Shard, Tekko-Kagi, Spear
    of the Magus, Dreamer''s Idol, Ancient Signet, Gluttonous Grimoire, Bracer of
    The Abyss, Polynomicon, Lernaean Bow, Dominance, Nimble Ring, Doom Orb, Silverbranch
    Bow, Chronos'' Pendant, The World Stone, Golden Blade, Blood-Bound Book, Soul
    Reaver, Arondight, Avatar''s Parashu, Toxic Blade, The Cosmic Horror, Rage, Gem
    of Focus, Heartwood Charm, Deathbringer, Demon Blade, Runeforged Hammer.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.56
      pick: 0.3
      fit: 0.44
    Death Metal:
      total: 0.56
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.59
    Spear of Desolation:
      total: 0.53
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.44
    The Crusher:
      total: 0.56
      efficiency: 0.51
      win: 0.67
      pick: 0.17
      fit: 0.51
    Titan's Bane:
      total: 0.57
      efficiency: 0.48
      win: 0.68
      pick: 0.35
      fit: 0.51
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.82
      win: 0.57
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Bragi's Harp
  - Tekko-Kagi
  - The Crusher
  flex_slots:
  - Bragi's Harp
  - The Crusher
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Death Metal, Tyrfing, Tekko-Kagi, Bragi''s
    Harp, Spear of Desolation, Lernaean Bow, Dominance, Silverbranch Bow, Soul Gem,
    Golden Blade, Obsidian Shard, Spear of the Magus, Toxic Blade, Demon Blade, Bracer
    of The Abyss, Rage, Dreamer''s Idol, Arondight, Avatar''s Parashu, Nimble Ring,
    Ancient Signet, Gluttonous Grimoire, Deathbringer, Polynomicon, Qin''s Blade,
    Riptalon, Doom Orb, Chronos'' Pendant, The World Stone, Pendulum Blade, Runeforged
    Hammer, Blood-Bound Book, Dagger of Frenzy.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.56
      pick: 0.3
      fit: 0.49
    Tyrfing:
      total: 0.55
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.69
    Death Metal:
      total: 0.55
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.51
    Bragi's Harp:
      total: 0.52
      efficiency: 0.47
      win: 0.57
      pick: 0.0
      fit: 0.66
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.49
      win: 0.57
      pick: 0.0
      fit: 0.69
    The Crusher:
      total: 0.57
      efficiency: 0.51
      win: 0.67
      pick: 0.17
      fit: 0.54
  community_ordered:
  - Jotunn's Revenge
  - The Crusher
  starter: *id001
---
