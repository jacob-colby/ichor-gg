---
type: smite-build
god: Medusa
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Tyrfing
    pick_rate: 0.3
    win_rate: 0.49
    alternates:
    - name: Transcendence
      pick_rate: 0.23
      win_rate: 0.54
    - name: Devourer's Gauntlet
      pick_rate: 0.1
      win_rate: 0.5
  - name: Sun Beam Bow
    pick_rate: 0.14
    win_rate: 0.48
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.12
      win_rate: 0.68
    - name: Dominance
      pick_rate: 0.12
      win_rate: 0.32
  - name: The Executioner
    pick_rate: 0.18
    win_rate: 0.57
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.14
      win_rate: 0.39
    - name: Dominance
      pick_rate: 0.14
      win_rate: 0.55
  - name: Riptalon
    pick_rate: 0.19
    win_rate: 0.57
    alternates:
    - name: The Executioner
      pick_rate: 0.12
      win_rate: 0.53
    - name: Heartseeker
      pick_rate: 0.1
      win_rate: 0.53
  - name: Dominance
    pick_rate: 0.1
    win_rate: 0.57
    alternates:
    - name: Titan's Bane
      pick_rate: 0.09
      win_rate: 0.62
    - name: Manchu Bow
      pick_rate: 0.09
      win_rate: 0.5
  - name: Hunter's Bow
    pick_rate: 0.13
    win_rate: 0.44
    alternates:
    - name: Manchu Bow
      pick_rate: 0.1
      win_rate: 0.14
    - name: Blinking Abyss
      pick_rate: 0.09
      win_rate: 0.83
  source_url: https://smitebrain.com/gods/medusa/
  last_verified: '2026-08-01'
  god_win_rate: 0.515527950310559
  god_matches_won: 83
  god_matches_played: 161
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Dominance
  - Gluttonous Grimoire
  - Riptalon
  - The Crusher
  flex_slots:
  - Dominance
  - Berserker's Shield
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Gluttonous Grimoire, The Crusher, Dominance, Berserker''s
    Shield, Soul Gem, Death Metal, Lernaean Bow, Damaru, Hydra''s Lament, Genji''s
    Guard, Golden Blade, Runeforged Hammer, Silverbranch Bow, The Reaper, Tekko-Kagi,
    Bragi''s Harp, Spear of the Magus, Breastplate of Valor, Bracer of The Abyss,
    Heartseeker, Pharaoh''s Curse, The Cosmic Horror, Amanita Charm, Demon Blade,
    Spear of Desolation, Oni Hunter''s Garb, Nimble Ring, Blood-Bound Book, Kinetic
    Cuirass, Yogi''s Necklace, Bancroft''s Talon, Shogun''s Ofuda, Avenging Blade,
    Obsidian Shard, Freya''s Tears, Eye of Providence, Chronos'' Pendant.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.66
      win: 0.68
      pick: 0.12
      fit: 0.39
    Dominance:
      total: 0.51
      efficiency: 0.54
      win: 0.57
      pick: 0.1
      fit: 0.39
    Gluttonous Grimoire:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.38
    Riptalon:
      total: 0.53
      efficiency: 0.56
      win: 0.57
      pick: 0.19
      fit: 0.47
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.4
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Riptalon
  - Damaru
  - Demon Blade
  - The Crusher
  flex_slots:
  - Damaru
  - Demon Blade
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
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Gluttonous Grimoire, The Crusher, Death Metal, Berserker''s
    Shield, Dominance, Soul Gem, Damaru, Lernaean Bow, Genji''s Guard, Hydra''s Lament,
    Golden Blade, Runeforged Hammer, The Reaper, Silverbranch Bow, Spear of the Magus,
    Breastplate of Valor, Bragi''s Harp, Tekko-Kagi, Heartseeker, Bracer of The Abyss,
    Pharaoh''s Curse, The Cosmic Horror, Demon Blade, Amanita Charm, Spear of Desolation,
    Oni Hunter''s Garb, Blood-Bound Book, Kinetic Cuirass, Yogi''s Necklace, Bancroft''s
    Talon, Nimble Ring, Obsidian Shard, Freya''s Tears, Avenging Blade, Eye of Providence,
    Chronos'' Pendant, Musashi''s Dual Swords.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.66
      win: 0.68
      pick: 0.12
      fit: 0.38
    Death Metal:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.46
    Riptalon:
      total: 0.53
      efficiency: 0.56
      win: 0.57
      pick: 0.19
      fit: 0.45
    Damaru:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.41
    Demon Blade:
      total: 0.46
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.63
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Titan's Bane
  - Berserker's Shield
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, Gluttonous Grimoire, Soul Gem, The Crusher, Death Metal,
    Berserker''s Shield, Dominance, Genji''s Guard, Hydra''s Lament, Spear of the
    Magus, Lernaean Bow, Spear of Desolation, The Cosmic Horror, Damaru, The Reaper,
    Breastplate of Valor, Runeforged Hammer, Heartseeker, Silverbranch Bow, Bracer
    of The Abyss, Bragi''s Harp, Golden Blade, Obsidian Shard, Tekko-Kagi, Chronos''
    Pendant, Blood-Bound Book, Bancroft''s Talon, Amanita Charm, Rod of Asclepius,
    Pharaoh''s Curse, Oni Hunter''s Garb, Kinetic Cuirass, Nimble Ring, Yogi''s Necklace,
    Helm of Radiance, Freya''s Tears, The World Stone, Doom Orb.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.17
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.66
      win: 0.68
      pick: 0.12
      fit: 0.46
    Death Metal:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.43
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.49
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.43
    Titan's Bane:
      total: 0.5
      efficiency: 0.48
      win: 0.62
      pick: 0.09
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Riptalon
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Soul Gem, Berserker''s Shield, Gluttonous
    Grimoire, Shield of the Phoenix, Rod of Asclepius, Kinetic Cuirass, Genji''s Guard,
    The Reaper, The Crusher, Eye of Providence, Blood-Bound Book, Bancroft''s Talon,
    Oni Hunter''s Garb, Chandra''s Grace, Runeforged Hammer, Pharaoh''s Curse, Death
    Metal, Golden Blade, Hydra''s Lament, Breastplate of Valor, Lernaean Bow, Damaru,
    Yogi''s Necklace, Freya''s Tears, Lifebinder, Phoenix Feather, Shogun''s Ofuda,
    Shifter''s Shield, Spectral Armor, Shield Splitter, Eye of the Storm, Erosion,
    Umbral Link, Spear of the Magus, Avenging Blade, Bloodforge, Silverbranch Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.16
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.38
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.66
      win: 0.68
      pick: 0.12
      fit: 0.27
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.42
    Riptalon:
      total: 0.56
      efficiency: 0.56
      win: 0.57
      pick: 0.19
      fit: 0.62
    Amanita Charm:
      total: 0.55
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.62
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Dominance
  - Riptalon
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Berserker's Shield
  - Dominance
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Gluttonous Grimoire, The Crusher, Soul Gem, Titan''s
    Bane, Berserker''s Shield, Dominance, Silverbranch Bow, Spear of the Magus, The
    Reaper, Death Metal, Avenging Blade, Genji''s Guard, Heartseeker, Lernaean Bow,
    Hydra''s Lament, Tekko-Kagi, The Cosmic Horror, Damaru, Spear of Desolation, Screeching
    Gargoyle, Runeforged Hammer, Golden Blade, Obsidian Shard, Breastplate of Valor,
    Bracer of The Abyss, Bragi''s Harp, Amanita Charm, Pharaoh''s Curse, Stone of
    Binding, Oni Hunter''s Garb, Kinetic Cuirass, Pendulum Blade, Yogi''s Necklace,
    Void Shield, Toxic Blade, The World Stone, Doom Orb.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.19
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.66
      win: 0.68
      pick: 0.12
      fit: 0.5
    Dominance:
      total: 0.5
      efficiency: 0.54
      win: 0.57
      pick: 0.1
      fit: 0.32
    Riptalon:
      total: 0.55
      efficiency: 0.56
      win: 0.57
      pick: 0.19
      fit: 0.56
    The Crusher:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.52
    Titan's Bane:
      total: 0.51
      efficiency: 0.48
      win: 0.62
      pick: 0.09
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Dominance
  - Gluttonous Grimoire
  - Riptalon
  - The Crusher
  flex_slots:
  - The Crusher
  - Dominance
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Gluttonous Grimoire, Berserker''s Shield, The Crusher,
    Dominance, Golden Blade, Soul Gem, Silverbranch Bow, Death Metal, Lernaean Bow,
    Genji''s Guard, Hydra''s Lament, Damaru, Runeforged Hammer, Breastplate of Valor,
    Bracer of The Abyss, Spear of the Magus, Pharaoh''s Curse, The Reaper, Bragi''s
    Harp, Tekko-Kagi, Amanita Charm, The Cosmic Horror, Oni Hunter''s Garb, Kinetic
    Cuirass, Yogi''s Necklace, Toxic Blade, Blood-Bound Book, Spear of Desolation,
    Nimble Ring, Bancroft''s Talon, Eye of Providence, Shogun''s Ofuda, Demon Blade,
    Freya''s Tears, Rod of Asclepius, Avenging Blade, Chronos'' Pendant.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.22
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.66
      win: 0.68
      pick: 0.12
      fit: 0.32
    Dominance:
      total: 0.5
      efficiency: 0.54
      win: 0.57
      pick: 0.1
      fit: 0.34
    Gluttonous Grimoire:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.33
    Riptalon:
      total: 0.55
      efficiency: 0.56
      win: 0.57
      pick: 0.19
      fit: 0.57
    The Crusher:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.34
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Hydra's Lament
  - The Crusher
  - Soul Gem
  flex_slots:
  - Berserker's Shield
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, Genji''s
    Guard, Gluttonous Grimoire, Hydra''s Lament, Berserker''s Shield, The Crusher,
    Breastplate of Valor, Dominance, Death Metal, Spear of Desolation, Chronos'' Pendant,
    Lernaean Bow, Damaru, Freya''s Tears, Shield of the Phoenix, Spear of the Magus,
    Runeforged Hammer, Bracer of The Abyss, Golden Blade, The Cosmic Horror, Silverbranch
    Bow, Gem of Focus, Arondight, Amanita Charm, Bragi''s Harp, Screeching Gargoyle,
    Pharaoh''s Curse, Chandra''s Grace, Blood-Bound Book, The Reaper, Oni Hunter''s
    Garb, Kinetic Cuirass, Bancroft''s Talon, Yogi''s Necklace, Pendulum Blade, Rod
    of Asclepius, Nimble Ring.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.28
    Berserker's Shield:
      total: 0.5
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.18
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.66
      win: 0.68
      pick: 0.12
      fit: 0.48
    Hydra's Lament:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.47
    The Crusher:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.3
    Soul Gem:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.65
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Dominance
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - Dominance
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Jotunn''s Revenge, Gluttonous Grimoire,
    Soul Gem, Death Metal, The Crusher, Berserker''s Shield, Dominance, Genji''s Guard,
    Spear of the Magus, Hydra''s Lament, The Cosmic Horror, Bracer of The Abyss, Lernaean
    Bow, Spear of Desolation, Bragi''s Harp, Damaru, Blood-Bound Book, Chronos'' Pendant,
    Bancroft''s Talon, Breastplate of Valor, Runeforged Hammer, Obsidian Shard, Rod
    of Asclepius, Golden Blade, Nimble Ring, Silverbranch Bow, The Reaper, Helm of
    Radiance, Jade Scepter, Amanita Charm, Pharaoh''s Curse, Tekko-Kagi, Oni Hunter''s
    Garb, Gem of Focus, Kinetic Cuirass, Yogi''s Necklace, The World Stone, Doom Orb.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.18
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.66
      win: 0.68
      pick: 0.12
      fit: 0.36
    Death Metal:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.5
    Dominance:
      total: 0.49
      efficiency: 0.54
      win: 0.57
      pick: 0.1
      fit: 0.29
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.51
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Dominance
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Dominance
  - Berserker's Shield
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Gluttonous Grimoire,
    Soul Gem, Death Metal, The Crusher, Dominance, Berserker''s Shield, Hydra''s Lament,
    Lernaean Bow, Damaru, Genji''s Guard, Spear of the Magus, Bragi''s Harp, The Cosmic
    Horror, Bracer of The Abyss, Runeforged Hammer, Golden Blade, The Reaper, Spear
    of Desolation, Heartseeker, Blood-Bound Book, Bancroft''s Talon, Silverbranch
    Bow, Tekko-Kagi, Breastplate of Valor, Obsidian Shard, Rod of Asclepius, Nimble
    Ring, Chronos'' Pendant, Amanita Charm, Helm of Radiance, Pharaoh''s Curse, Oni
    Hunter''s Garb, Jade Scepter, Kinetic Cuirass, Yogi''s Necklace, Avenging Blade,
    The World Stone.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.18
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.66
      win: 0.68
      pick: 0.12
      fit: 0.39
    Death Metal:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.53
    Dominance:
      total: 0.5
      efficiency: 0.54
      win: 0.57
      pick: 0.1
      fit: 0.36
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.48
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - The Crusher
  - Soul Gem
  flex_slots:
  - Soul Gem
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Jotunn''s Revenge, The Crusher,
    Berserker''s Shield, Soul Gem, Death Metal, Lernaean Bow, Damaru, Hydra''s Lament,
    Genji''s Guard, Golden Blade, Runeforged Hammer, Silverbranch Bow, The Reaper,
    Dominance, Tekko-Kagi, Bragi''s Harp, Spear of the Magus, Breastplate of Valor,
    Bracer of The Abyss, Pharaoh''s Curse, The Cosmic Horror, Amanita Charm, Demon
    Blade, Spear of Desolation, Oni Hunter''s Garb, Nimble Ring, Blood-Bound Book,
    Kinetic Cuirass, Yogi''s Necklace, Bancroft''s Talon, Heartseeker, Shogun''s Ofuda,
    Avenging Blade, Obsidian Shard, Freya''s Tears, Eye of Providence, Chronos'' Pendant.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.24
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.66
      win: 0.68
      pick: 0.12
      fit: 0.39
    Death Metal:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.43
    Gluttonous Grimoire:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.38
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.4
    Soul Gem:
      total: 0.5
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.48
  starter: *id001
---
