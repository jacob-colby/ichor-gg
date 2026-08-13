---
type: smite-build
god: Xbalanque
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Nightstalker
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.5
  slot_order:
  - name: Tyrfing
    pick_rate: 0.65
    win_rate: 0.58
    alternates:
    - name: Transcendence
      pick_rate: 0.08
      win_rate: 0.5
    - name: Book of Thoth
      pick_rate: 0.07
      win_rate: 0.71
  - name: Odysseus' Bow
    pick_rate: 0.52
    win_rate: 0.57
    alternates:
    - name: Dominance
      pick_rate: 0.09
      win_rate: 0.44
    - name: Spear of Desolation
      pick_rate: 0.07
      win_rate: 0.71
  - name: Hastened Fatalis
    pick_rate: 0.18
    win_rate: 0.72
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.17
      win_rate: 0.59
    - name: The Executioner
      pick_rate: 0.12
      win_rate: 0.58
  - name: Riptalon
    pick_rate: 0.24
    win_rate: 0.63
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.16
      win_rate: 0.69
    - name: The Executioner
      pick_rate: 0.15
      win_rate: 0.47
  - name: Silverbranch Bow
    pick_rate: 0.25
    win_rate: 0.67
    alternates:
    - name: The Executioner
      pick_rate: 0.16
      win_rate: 0.67
    - name: Hunter's Bow
      pick_rate: 0.09
      win_rate: 0.56
  - name: Hunter's Bow
    pick_rate: 0.12
    win_rate: 0.44
    alternates:
    - name: Manchu Bow
      pick_rate: 0.12
      win_rate: 0.56
    - name: Hastened Fatalis
      pick_rate: 0.12
      win_rate: 0.56
  community_starters:
  - name: Death's Embrace
    pick_rate: 0.58
    win_rate: 0.61
  - name: Death's Toll
    pick_rate: 0.17
    win_rate: 0.35
  - name: Sharpshooter's Arrow
    pick_rate: 0.06
    win_rate: 0.83
  source_url: https://smitebrain.com/gods/xbalanque/
  last_verified: '2026-08-13'
  god_win_rate: 0.5686274509803921
  god_matches_won: 58
  god_matches_played: 102
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-13'
  god_matches_analyzed: 2102
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Lernaean Bow
  - Berserker's Shield
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  - Damaru
  flex_slots:
  - Damaru
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Lernaean Bow, Damaru, Golden Blade, The Crusher,
    Demon Blade, Jotunn''s Revenge, Pharaoh''s Curse, Hydra''s Lament, Genji''s Guard,
    Deathbringer, Runeforged Hammer, Tekko-Kagi, Shogun''s Ofuda, Breastplate of Valor,
    The Reaper, Musashi''s Dual Swords, Eros'' Bow, Kinetic Cuirass, Amanita Charm,
    Rage, Oni Hunter''s Garb, Eye of Providence, Avenging Blade, Shield Splitter,
    Dominance.'
  slot_scores:
    Lernaean Bow:
      total: 0.56
      efficiency: 0.54
      win: 0.6
      pick: 0.0
      fit: 0.64
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.33
    Tyrfing:
      total: 0.55
      efficiency: 0.46
      win: 0.58
      pick: 0.65
      fit: 0.64
    Riptalon:
      total: 0.57
      efficiency: 0.56
      win: 0.63
      pick: 0.4
      fit: 0.46
    Silverbranch Bow:
      total: 0.57
      efficiency: 0.54
      win: 0.67
      pick: 0.54
      fit: 0.33
    Damaru:
      total: 0.56
      efficiency: 0.58
      win: 0.6
      pick: 0.0
      fit: 0.54
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: crit
  slot_order:
  - Berserker's Shield
  - Riptalon
  - Silverbranch Bow
  - Damaru
  - Demon Blade
  - Deathbringer
  flex_slots:
  - Demon Blade
  - Deathbringer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Damaru, Berserker''s Shield, Lernaean Bow, The Crusher, Golden Blade,
    Demon Blade, Jotunn''s Revenge, Genji''s Guard, Hydra''s Lament, Pharaoh''s Curse,
    Deathbringer, Runeforged Hammer, Musashi''s Dual Swords, Tekko-Kagi, Breastplate
    of Valor, The Reaper, Shogun''s Ofuda, Rage, Kinetic Cuirass, Eros'' Bow, Amanita
    Charm, Oni Hunter''s Garb, Eye of Providence, Avenging Blade, Shield Splitter,
    Dominance.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.3
    Riptalon:
      total: 0.56
      efficiency: 0.56
      win: 0.63
      pick: 0.4
      fit: 0.42
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.54
      win: 0.67
      pick: 0.54
      fit: 0.3
    Damaru:
      total: 0.56
      efficiency: 0.58
      win: 0.6
      pick: 0.0
      fit: 0.57
    Demon Blade:
      total: 0.53
      efficiency: 0.37
      win: 0.6
      pick: 0.0
      fit: 0.88
    Deathbringer:
      total: 0.52
      efficiency: 0.45
      win: 0.6
      pick: 0.0
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Riptalon
  - Silverbranch Bow
  - Amanita Charm
  - Pharaoh's Curse
  flex_slots:
  - Silverbranch Bow
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Shield of the Phoenix, Kinetic Cuirass,
    Pharaoh''s Curse, Genji''s Guard, Oni Hunter''s Garb, Golden Blade, The Reaper,
    Shogun''s Ofuda, The Crusher, Lernaean Bow, Chandra''s Grace, Damaru, Breastplate
    of Valor, Runeforged Hammer, Jotunn''s Revenge, Phoenix Feather, Spectral Armor,
    Freya''s Tears, Shifter''s Shield, Erosion, Umbral Link, Eye of Providence, Eye
    of the Storm, Hydra''s Lament, Shield Splitter, Draconic Scale.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.5
    Riptalon:
      total: 0.59
      efficiency: 0.56
      win: 0.63
      pick: 0.4
      fit: 0.58
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.54
      win: 0.67
      pick: 0.54
      fit: 0.2
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.7
    Pharaoh's Curse:
      total: 0.54
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Riptalon
  - Silverbranch Bow
  - Tekko-Kagi
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    for this god: The Crusher, Jotunn''s Revenge, Berserker''s Shield, The Reaper,
    Tekko-Kagi, Lernaean Bow, Damaru, Genji''s Guard, Avenging Blade, Heartseeker,
    Golden Blade, Hydra''s Lament, Pharaoh''s Curse, Screeching Gargoyle, Breastplate
    of Valor, Toxic Blade, Titan''s Bane, Stone of Binding, Runeforged Hammer, Kinetic
    Cuirass, Void Shield, Amanita Charm, Oni Hunter''s Garb, Demon Blade, Shogun''s
    Ofuda, Dominance.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.22
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.47
    Riptalon:
      total: 0.6
      efficiency: 0.56
      win: 0.63
      pick: 0.4
      fit: 0.64
    Silverbranch Bow:
      total: 0.6
      efficiency: 0.54
      win: 0.67
      pick: 0.54
      fit: 0.56
    Tekko-Kagi:
      total: 0.53
      efficiency: 0.45
      win: 0.6
      pick: 0.0
      fit: 0.69
    The Crusher:
      total: 0.58
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Berserker's Shield
  - Tyrfing
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Berserker's Shield
  - Lernaean Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    this god: Golden Blade, Berserker''s Shield, Lernaean Bow, Damaru, The Crusher,
    Jotunn''s Revenge, Genji''s Guard, Pharaoh''s Curse, Hydra''s Lament, Demon Blade,
    Breastplate of Valor, Runeforged Hammer, Shogun''s Ofuda, Tekko-Kagi, Kinetic
    Cuirass, Eros'' Bow, Amanita Charm, Toxic Blade, Deathbringer, The Reaper, Oni
    Hunter''s Garb, Qin''s Blade, Eye of Providence, Musashi''s Dual Swords, Yogi''s
    Necklace, Dominance.'
  slot_scores:
    Golden Blade:
      total: 0.56
      efficiency: 0.54
      win: 0.6
      pick: 0.0
      fit: 0.65
    Lernaean Bow:
      total: 0.54
      efficiency: 0.54
      win: 0.6
      pick: 0.0
      fit: 0.55
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.29
    Tyrfing:
      total: 0.57
      efficiency: 0.46
      win: 0.58
      pick: 0.65
      fit: 0.75
    Riptalon:
      total: 0.59
      efficiency: 0.56
      win: 0.63
      pick: 0.4
      fit: 0.59
    Silverbranch Bow:
      total: 0.59
      efficiency: 0.54
      win: 0.67
      pick: 0.54
      fit: 0.49
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Riptalon
  - Silverbranch Bow
  flex_slots:
  - Silverbranch Bow
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Jotunn''s Revenge,
    Hydra''s Lament, Breastplate of Valor, Berserker''s Shield, Freya''s Tears, The
    Crusher, Lernaean Bow, Damaru, Shield of the Phoenix, Screeching Gargoyle, Golden
    Blade, Pharaoh''s Curse, Chandra''s Grace, Arondight, Kinetic Cuirass, Runeforged
    Hammer, Amanita Charm, Oni Hunter''s Garb, Eye of Providence, Shogun''s Ofuda,
    Eros'' Bow, Yogi''s Necklace, The Reaper, Demon Blade, Dominance.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.6
      pick: 0.0
      fit: 0.32
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.41
    Hydra's Lament:
      total: 0.55
      efficiency: 0.58
      win: 0.6
      pick: 0.0
      fit: 0.51
    Riptalon:
      total: 0.54
      efficiency: 0.56
      win: 0.63
      pick: 0.4
      fit: 0.29
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.54
      win: 0.67
      pick: 0.54
      fit: 0.21
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - Spear of Desolation
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - Death Metal
  - The Crusher
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Gluttonous Grimoire, Spear of Desolation,
    Soul Gem, Jotunn''s Revenge, Death Metal, The Crusher, Berserker''s Shield, Genji''s
    Guard, Spear of the Magus, The Cosmic Horror, Bracer of The Abyss, Hydra''s Lament,
    Breastplate of Valor, Lernaean Bow, Damaru, Blood-Bound Book, Bancroft''s Talon,
    Bragi''s Harp, Chronos'' Pendant, Obsidian Shard, Nimble Ring, Helm of Radiance,
    Golden Blade, Rod of Asclepius, The Reaper, Pharaoh''s Curse, Jade Scepter, Gem
    of Focus, Runeforged Hammer, The World Stone, Doom Orb, Kinetic Cuirass, Freya''s
    Tears, Tekko-Kagi, Amanita Charm, Dreamer''s Idol, Ancient Signet, Dominance.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.36
    Death Metal:
      total: 0.55
      efficiency: 0.58
      win: 0.6
      pick: 0.0
      fit: 0.5
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.52
    Spear of Desolation:
      total: 0.58
      efficiency: 0.52
      win: 0.71
      pick: 0.1
      fit: 0.46
    Silverbranch Bow:
      total: 0.57
      efficiency: 0.54
      win: 0.67
      pick: 0.54
      fit: 0.32
    The Crusher:
      total: 0.54
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - Spear of Desolation
  - Silverbranch Bow
  - The Crusher
  flex_slots:
  - The Crusher
  - Jotunn's Revenge
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Death Metal,
    Spear of Desolation, The Crusher, Soul Gem, Jotunn''s Revenge, Berserker''s Shield,
    Spear of the Magus, Lernaean Bow, Damaru, The Cosmic Horror, Bracer of The Abyss,
    Bragi''s Harp, Genji''s Guard, Golden Blade, Hydra''s Lament, The Reaper, Blood-Bound
    Book, Bancroft''s Talon, Obsidian Shard, Nimble Ring, Tekko-Kagi, Runeforged Hammer,
    Breastplate of Valor, Pharaoh''s Curse, Helm of Radiance, Rod of Asclepius, Kinetic
    Cuirass, Chronos'' Pendant, Heartseeker, Jade Scepter, The World Stone, Doom Orb,
    Amanita Charm, Dreamer''s Idol, Oni Hunter''s Garb, Dominance.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.34
    Death Metal:
      total: 0.56
      efficiency: 0.58
      win: 0.6
      pick: 0.0
      fit: 0.57
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.52
    Spear of Desolation:
      total: 0.56
      efficiency: 0.52
      win: 0.71
      pick: 0.1
      fit: 0.34
    Silverbranch Bow:
      total: 0.57
      efficiency: 0.54
      win: 0.67
      pick: 0.54
      fit: 0.35
    The Crusher:
      total: 0.56
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Berserker's Shield
  - Riptalon
  - Damaru
  - The Crusher
  flex_slots:
  - The Crusher
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Lernaean Bow, Damaru, Golden Blade,
    The Crusher, Demon Blade, Jotunn''s Revenge, Dominance, Pharaoh''s Curse, Hydra''s
    Lament, Genji''s Guard, Deathbringer, Runeforged Hammer, Tekko-Kagi, Shogun''s
    Ofuda, Breastplate of Valor, The Reaper, Musashi''s Dual Swords, Eros'' Bow, Kinetic
    Cuirass, Amanita Charm, Rage, Oni Hunter''s Garb, Eye of Providence, Avenging
    Blade, Shield Splitter.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.54
      win: 0.6
      pick: 0.0
      fit: 0.54
    Lernaean Bow:
      total: 0.56
      efficiency: 0.54
      win: 0.6
      pick: 0.0
      fit: 0.64
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.33
    Riptalon:
      total: 0.57
      efficiency: 0.56
      win: 0.63
      pick: 0.4
      fit: 0.46
    Damaru:
      total: 0.56
      efficiency: 0.58
      win: 0.6
      pick: 0.0
      fit: 0.54
    The Crusher:
      total: 0.54
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.31
  starter: *id001
---
