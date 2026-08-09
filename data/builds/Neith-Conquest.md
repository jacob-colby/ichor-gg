---
type: smite-build
god: Neith
mode: Conquest
builds:
- source: community
  aspect: Aspect of Wind
  aspect_pick_rate: 0.34
  aspect_win_rate: 0.51
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.28
    win_rate: 0.51
    alternates:
    - name: Book of Thoth
      pick_rate: 0.18
      win_rate: 0.44
    - name: Tyrfing
      pick_rate: 0.13
      win_rate: 0.48
  - name: Book of Thoth
    pick_rate: 0.14
    win_rate: 0.44
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.15
      win_rate: 0.45
    - name: The World Stone
      pick_rate: 0.11
      win_rate: 0.54
  - name: Soul Gem
    pick_rate: 0.16
    win_rate: 0.52
    alternates:
    - name: The World Stone
      pick_rate: 0.1
      win_rate: 0.51
    - name: Rod of Tahuti
      pick_rate: 0.08
      win_rate: 0.48
  - name: Rod of Tahuti
    pick_rate: 0.22
    win_rate: 0.51
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.14
      win_rate: 0.46
    - name: Silverbranch Bow
      pick_rate: 0.07
      win_rate: 0.57
  - name: Obsidian Shard
    pick_rate: 0.13
    win_rate: 0.54
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.12
      win_rate: 0.52
    - name: Evil Eye
      pick_rate: 0.07
      win_rate: 0.39
  - name: Void Shard
    pick_rate: 0.09
    win_rate: 0.47
    alternates:
    - name: Evil Eye
      pick_rate: 0.09
      win_rate: 0.52
    - name: Obsidian Shard
      pick_rate: 0.08
      win_rate: 0.44
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.27
    win_rate: 0.51
  - name: Conduit Gem
    pick_rate: 0.17
    win_rate: 0.38
  - name: Death's Embrace
    pick_rate: 0.08
    win_rate: 0.52
  source_url: https://smitebrain.com/gods/neith/
  last_verified: '2026-08-09'
  god_win_rate: 0.47596153846153844
  god_matches_won: 297
  god_matches_played: 624
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-09'
  god_matches_analyzed: 15881
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - The Crusher
  - Soul Gem
  flex_slots:
  - Death Metal
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
    this god: Gluttonous Grimoire, Jotunn''s Revenge, The Crusher, Death Metal, Berserker''s
    Shield, Silverbranch Bow, Genji''s Guard, Lernaean Bow, Riptalon, Hydra''s Lament,
    Damaru, Obsidian Shard, Spear of the Magus, Bracer of The Abyss, The Cosmic Horror,
    Bragi''s Harp, Runeforged Hammer, Golden Blade, Breastplate of Valor, The Reaper,
    Blood-Bound Book, Bancroft''s Talon, Dominance, Nimble Ring, Tekko-Kagi, Pharaoh''s
    Curse, Chronos'' Pendant, Amanita Charm, Rod of Asclepius, Oni Hunter''s Garb,
    Tyrfing, Helm of Radiance, Yogi''s Necklace, Kinetic Cuirass, Jade Scepter, Freya''s
    Tears, Heartseeker, Dreamer''s Idol.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.2
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.36
    Death Metal:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.49
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.48
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.38
    Soul Gem:
      total: 0.53
      efficiency: 0.59
      win: 0.52
      pick: 0.16
      fit: 0.56
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Damaru
  - Demon Blade
  - The Crusher
  - Soul Gem
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
    this god: Gluttonous Grimoire, Death Metal, Jotunn''s Revenge, The Crusher, Berserker''s
    Shield, Silverbranch Bow, Genji''s Guard, Damaru, Hydra''s Lament, Obsidian Shard,
    Lernaean Bow, Riptalon, Spear of the Magus, The Cosmic Horror, Bracer of The Abyss,
    Bragi''s Harp, Runeforged Hammer, Breastplate of Valor, Golden Blade, The Reaper,
    Blood-Bound Book, Bancroft''s Talon, Dominance, Nimble Ring, Chronos'' Pendant,
    Amanita Charm, Rod of Asclepius, Pharaoh''s Curse, Tekko-Kagi, Oni Hunter''s Garb,
    Yogi''s Necklace, Helm of Radiance, Kinetic Cuirass, Tyrfing, Jade Scepter, Freya''s
    Tears, Demon Blade, Eye of Providence.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.35
    Death Metal:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.51
    Damaru:
      total: 0.49
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.36
    Demon Blade:
      total: 0.44
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.54
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.37
    Soul Gem:
      total: 0.53
      efficiency: 0.59
      win: 0.52
      pick: 0.16
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Silverbranch Bow
  - The Crusher
  - Soul Gem
  flex_slots:
  - Death Metal
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
    god: Gluttonous Grimoire, Jotunn''s Revenge, The Crusher, Silverbranch Bow, Death
    Metal, Berserker''s Shield, Genji''s Guard, Hydra''s Lament, Obsidian Shard, Spear
    of the Magus, Riptalon, Lernaean Bow, Damaru, The Cosmic Horror, Breastplate of
    Valor, The Reaper, Runeforged Hammer, The World Stone, Bracer of The Abyss, Bragi''s
    Harp, Golden Blade, Chronos'' Pendant, Tekko-Kagi, Blood-Bound Book, Bancroft''s
    Talon, Dominance, Amanita Charm, Oni Hunter''s Garb, Pharaoh''s Curse, Rod of
    Asclepius, Yogi''s Necklace, Kinetic Cuirass, Heartseeker, Freya''s Tears, Nimble
    Ring, Tyrfing, Helm of Radiance, Dreamer''s Idol.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.17
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.46
    Death Metal:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.43
    Silverbranch Bow:
      total: 0.5
      efficiency: 0.54
      win: 0.57
      pick: 0.07
      fit: 0.37
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.43
    Soul Gem:
      total: 0.54
      efficiency: 0.59
      win: 0.52
      pick: 0.16
      fit: 0.63
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - The Crusher
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - The Crusher
  - Kinetic Cuirass
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
    this god: Amanita Charm, Gluttonous Grimoire, Berserker''s Shield, Rod of Asclepius,
    Riptalon, Shield of the Phoenix, Blood-Bound Book, Genji''s Guard, Bancroft''s
    Talon, The Crusher, The Reaper, Kinetic Cuirass, Jotunn''s Revenge, Death Metal,
    Eye of Providence, Oni Hunter''s Garb, Chandra''s Grace, Runeforged Hammer, Pharaoh''s
    Curse, Breastplate of Valor, Lifebinder, Hydra''s Lament, Golden Blade, Lernaean
    Bow, Damaru, Spear of the Magus, Yogi''s Necklace, Freya''s Tears, Phoenix Feather,
    Spectral Armor, Shifter''s Shield, Shogun''s Ofuda, The Cosmic Horror, Bracer
    of The Abyss, Helm of Radiance, Jade Scepter, Umbral Link, Shield Splitter, Bragi''s
    Harp.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.15
    Berserker's Shield:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.39
    The Crusher:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.3
    Amanita Charm:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.59
    Soul Gem:
      total: 0.56
      efficiency: 0.59
      win: 0.52
      pick: 0.16
      fit: 0.73
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Spear of Desolation
  - Silverbranch Bow
  - The Crusher
  - Soul Gem
  flex_slots:
  - Berserker's Shield
  - Spear of Desolation
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
    for this god: Gluttonous Grimoire, The Crusher, Jotunn''s Revenge, Silverbranch
    Bow, Berserker''s Shield, Obsidian Shard, Death Metal, Riptalon, Spear of the
    Magus, The Cosmic Horror, Genji''s Guard, Avenging Blade, The World Stone, Hydra''s
    Lament, The Reaper, Lernaean Bow, Damaru, Tekko-Kagi, Bracer of The Abyss, Screeching
    Gargoyle, Runeforged Hammer, Breastplate of Valor, Bragi''s Harp, Golden Blade,
    Blood-Bound Book, Heartseeker, Bancroft''s Talon, Dreamer''s Idol, Amanita Charm,
    Doom Orb, Dominance, Oni Hunter''s Garb, Pharaoh''s Curse, Stone of Binding, Rod
    of Asclepius, Chronos'' Pendant, Yogi''s Necklace, Nimble Ring.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.17
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
    Spear of Desolation:
      total: 0.5
      efficiency: 0.52
      win: 0.51
      pick: 0.28
      fit: 0.47
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.54
      win: 0.57
      pick: 0.07
      fit: 0.44
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Soul Gem:
      total: 0.54
      efficiency: 0.59
      win: 0.52
      pick: 0.16
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Riptalon
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
    this god: Gluttonous Grimoire, Silverbranch Bow, Berserker''s Shield, The Crusher,
    Jotunn''s Revenge, Riptalon, Death Metal, Genji''s Guard, Golden Blade, Lernaean
    Bow, Hydra''s Lament, Obsidian Shard, Damaru, Spear of the Magus, Bracer of The
    Abyss, Tyrfing, The Cosmic Horror, Runeforged Hammer, Bragi''s Harp, Breastplate
    of Valor, Blood-Bound Book, Dominance, Bancroft''s Talon, Pharaoh''s Curse, The
    Reaper, Amanita Charm, Nimble Ring, Oni Hunter''s Garb, Rod of Asclepius, Chronos''
    Pendant, Yogi''s Necklace, Kinetic Cuirass, Tekko-Kagi, Helm of Radiance, Jade
    Scepter, Eye of Providence, Toxic Blade, Freya''s Tears.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.2
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.3
    Riptalon:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.52
    Silverbranch Bow:
      total: 0.52
      efficiency: 0.54
      win: 0.57
      pick: 0.07
      fit: 0.46
    The Crusher:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.33
    Soul Gem:
      total: 0.52
      efficiency: 0.59
      win: 0.52
      pick: 0.16
      fit: 0.49
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Hydra's Lament
  - Spear of Desolation
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Berserker's Shield
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Genji''s Guard,
    Gluttonous Grimoire, Hydra''s Lament, Berserker''s Shield, The Crusher, Breastplate
    of Valor, Silverbranch Bow, Death Metal, Riptalon, Chronos'' Pendant, Lernaean
    Bow, Damaru, Freya''s Tears, Obsidian Shard, Spear of the Magus, Shield of the
    Phoenix, Runeforged Hammer, Bracer of The Abyss, The Cosmic Horror, Golden Blade,
    Gem of Focus, Amanita Charm, Arondight, The Reaper, Pharaoh''s Curse, Oni Hunter''s
    Garb, Screeching Gargoyle, Chandra''s Grace, Blood-Bound Book, Bragi''s Harp,
    Yogi''s Necklace, Dominance, Kinetic Cuirass, Bancroft''s Talon, Pendulum Blade,
    Rod of Asclepius, Tyrfing.'
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
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.49
    Hydra's Lament:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.46
    Spear of Desolation:
      total: 0.5
      efficiency: 0.52
      win: 0.51
      pick: 0.28
      fit: 0.49
    Soul Gem:
      total: 0.55
      efficiency: 0.59
      win: 0.52
      pick: 0.16
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Silverbranch Bow
  - The Crusher
  - Soul Gem
  flex_slots:
  - Berserker's Shield
  - Silverbranch Bow
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
    + win/pick). Underrated for this god: Gluttonous Grimoire, Death Metal, Jotunn''s
    Revenge, The Crusher, Berserker''s Shield, Silverbranch Bow, Genji''s Guard, Obsidian
    Shard, Spear of the Magus, Hydra''s Lament, The Cosmic Horror, Bracer of The Abyss,
    Lernaean Bow, Riptalon, Damaru, Bragi''s Harp, The World Stone, Blood-Bound Book,
    Breastplate of Valor, Chronos'' Pendant, Bancroft''s Talon, Runeforged Hammer,
    Rod of Asclepius, Nimble Ring, Golden Blade, The Reaper, Helm of Radiance, Amanita
    Charm, Jade Scepter, Dominance, Pharaoh''s Curse, Oni Hunter''s Garb, Yogi''s
    Necklace, Gem of Focus, Tekko-Kagi, Kinetic Cuirass, Dreamer''s Idol, Tyrfing.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.18
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.36
    Death Metal:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.5
    Silverbranch Bow:
      total: 0.5
      efficiency: 0.54
      win: 0.57
      pick: 0.07
      fit: 0.32
    The Crusher:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.35
    Soul Gem:
      total: 0.54
      efficiency: 0.59
      win: 0.52
      pick: 0.16
      fit: 0.63
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Silverbranch Bow
  - The Crusher
  - Soul Gem
  flex_slots:
  - Berserker's Shield
  - Silverbranch Bow
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
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, The Crusher,
    Death Metal, Jotunn''s Revenge, Berserker''s Shield, Silverbranch Bow, Hydra''s
    Lament, Lernaean Bow, Genji''s Guard, Damaru, Obsidian Shard, Spear of the Magus,
    Riptalon, Bragi''s Harp, Bracer of The Abyss, Runeforged Hammer, The Cosmic Horror,
    Golden Blade, The Reaper, Blood-Bound Book, Breastplate of Valor, Dominance, Bancroft''s
    Talon, Tekko-Kagi, Nimble Ring, Chronos'' Pendant, Rod of Asclepius, Tyrfing,
    Amanita Charm, Pharaoh''s Curse, Helm of Radiance, Oni Hunter''s Garb, Yogi''s
    Necklace, Kinetic Cuirass, Jade Scepter, Heartseeker, Avenging Blade, Dreamer''s
    Idol.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.18
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.53
    Silverbranch Bow:
      total: 0.5
      efficiency: 0.54
      win: 0.57
      pick: 0.07
      fit: 0.33
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.41
    Soul Gem:
      total: 0.53
      efficiency: 0.59
      win: 0.52
      pick: 0.16
      fit: 0.56
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
  - Death Metal
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Jotunn''s Revenge, The Crusher,
    Death Metal, Berserker''s Shield, Genji''s Guard, Lernaean Bow, Riptalon, Hydra''s
    Lament, Damaru, Spear of the Magus, Bracer of The Abyss, The Cosmic Horror, Bragi''s
    Harp, Runeforged Hammer, Golden Blade, Silverbranch Bow, Breastplate of Valor,
    The Reaper, Blood-Bound Book, Bancroft''s Talon, Dominance, Nimble Ring, Obsidian
    Shard, Tekko-Kagi, Pharaoh''s Curse, Chronos'' Pendant, Amanita Charm, Tyrfing,
    Rod of Asclepius, Oni Hunter''s Garb, Helm of Radiance, Yogi''s Necklace, Kinetic
    Cuirass, Jade Scepter, Freya''s Tears, Heartseeker, Dreamer''s Idol.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.2
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.36
    Death Metal:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.49
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.48
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.38
    Soul Gem:
      total: 0.53
      efficiency: 0.59
      win: 0.52
      pick: 0.16
      fit: 0.56
  starter: *id001
---
